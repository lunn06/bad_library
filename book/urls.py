from django.urls import path

from . import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("detail/<slug:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("search/", views.book_search, name="book_search"),

    path("author/detail/<slug:pk>/", views.AuthorDetailView.as_view(), name="author_detail"),
    path("author/", views.AuthorListView.as_view(), name="author_list"),

    path("genre/detail/<slug:pk>/", views.GenreDetailView.as_view(), name="genre_detail"),
    path("genre/", views.GenreListView.as_view(), name="genre_list"),
]
