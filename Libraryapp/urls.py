from django.contrib import admin
from django.urls import path
from .views import helloView, addBookView, addBook, editBookView, editBook, deleteBookView

urlpatterns = [
    path("", helloView, name="hello"),
    path("add-book/", addBookView, name="add_book_view"),
    path("add-book/add/", addBook, name="add_book"),
    path("edit-book/", editBookView, name="edit_book_view"),
    path("edit-book/edit/", editBook, name="edit_book"),
    path("delete-book/", deleteBookView, name="delete_book_view")
]
