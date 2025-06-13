from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView

from book.models import Book, Author, Genre


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'


class GenreListView(ListView):
    model = Genre
    template_name = 'genre_list.html'
    context_object_name = 'genres'


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genre_detail.html'
    context_object_name = 'genre'


def book_search(request):
    # Получаем все жанры для выпадающего списка
    all_genres = Genre.objects.all()

    # Получаем параметры поиска
    query = request.GET.get('q', '')
    author_query = request.GET.get('author', '')
    genre_name = request.GET.get('genre', '')

    # Начинаем с полного набора книг
    books = Book.objects.all()

    # Применяем фильтры
    if query:
        books = books.filter(title__icontains=query)
    if author_query:
        books = books.filter(authors__name__icontains=author_query)
    if genre_name:
        books = books.filter(genres__name__icontains=genre_name)

    context = {
        'books': books,
        'all_genres': all_genres,
        'request': request,
        'is_not_found': books.count() == 0,
    }
    return render(request, 'book_search_result.html', context)
