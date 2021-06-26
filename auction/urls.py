from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auction/<int:id>", views.item, name="item"),
    path("watchlist_add/<int:id>", views.watchlist_toggle, name="watchlist_toggle"),
    path("auction/<int:id>/bid", views.item_bid, name="bid"),
    path("auction/<int:id>/close", views.item_close, name="close"),
    path("auction/<int:id>/comment", views.comment, name="comment"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories_list", views.categories_list, name="categories_list"),
    path("categories/<str:name>", views.category, name="category"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create")  
]