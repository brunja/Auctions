from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Category, Item, Bid, Comment
from .forms import ItemForm, BidForm, CommentForm


def index(request):
    return render(request, "auction/index.html", {
        "items": Item.objects.all().filter(active=True),
        "bids": Bid.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auction/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auction/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auction/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auction/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auction/register.html")

@login_required(login_url="login")
def create(request):
    form = ItemForm()
    if request.method == "POST":
        if request.user.is_authenticated:
            form = ItemForm(request.POST)
            if form.is_valid():
                new_item = form.save(commit=False)
                new_item.user = request.user
                new_item.save()
                return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auction/create.html", {
            "message": "You need to be logged in to create an auction!"
            })
            
    context = {'form':form}
    return render(request, "auction/create.html", context)

def item(request, id):
    if request.method == "GET":
        if request.user is None:
            return redirect('login_view')
        item = Item.objects.get(id=id)
        comments = Comment.objects.all().filter(item=item)
        bids = Bid.objects.all()
        highest_bid = bids.filter(item=item).order_by('-amount').first
        return render(request, 'auction/item.html', {
            'item': item,
            'bid_form': BidForm(),
            'comment_form': CommentForm(),
            'highest_bid': highest_bid,
            'comments': comments
        })

@login_required(login_url="login")
def watchlist_toggle(request, id):
    if request.method == "POST":
        item = Item.objects.get(id=id)
        watchlist = request.user.watchlist
        if item in watchlist.all():
            watchlist.remove(item)
        else:
            watchlist.add(item)

        return HttpResponseRedirect(reverse('item', kwargs={'id': id}))

@login_required(login_url="login")
def watchlist(request):
    context = {
        "watchlist": request.user.watchlist.all(),
    }
    return render(request, "auction/watchlist.html", context)

@login_required(login_url="login")
def item_bid(request, id):
    bid_form = BidForm(request.POST or None)
    #Bid submission form
    if bid_form.is_valid():
        item = Item.objects.get(id=id)
        user = request.user
        new_bid = bid_form.save(commit=False)
        bids = Bid.objects.filter(item=item)
        is_highest_bid = all(new_bid.amount > n.amount for n in bids)
        is_valid_first_bid = new_bid.amount >= item.price

        if is_highest_bid and is_valid_first_bid:
            new_bid.item = item
            new_bid.user = request.user
            new_bid.save()
            
        else:
            return render(request, "auction/item.html", {
                "item": item,
                "message": "Your bid should be higher!",
                "watchlist": request.user.watchlist.all()
            })
    return HttpResponseRedirect(reverse("item", kwargs={"id": id}))

@login_required(login_url="auction/login")
def item_close(request, id):
    item = Item.objects.get(id=id)
    if request.user == item.user:
        item.active = False
        item.save()
    return HttpResponseRedirect(reverse("item", kwargs={"id" : id}))

def category(request, name):
    category = Category.objects.get(name=name)
    items = Item.objects.filter(
        category=category,
        active=True
    )
    return render(request, "auction/category.html", {
        "items": items,
        "title": category.name
    })

def categories_list(request):
    return render(request, "auction/categories_list.html", {
        "categories": Category.objects.all()
    })

def comment(request, id):
    comment_form = CommentForm(request.POST or None)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.item = Item.objects.get(id=id)
        comment.user = request.user
        comment.save()
    
    return HttpResponseRedirect(reverse('item', kwargs={'id': id}))

