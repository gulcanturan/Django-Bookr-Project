from django.urls import path, include


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("books/", views.books, name="books"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
]
