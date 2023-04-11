from project.repositories.book_repository import BookRepository
from project.repositories.base_repository import mysql_db
import logging


class BookService():

    def list_book(self):
        book = BookRepository().list_book()
        return {"book": book}

    def get_book(self, id):
        book = BookRepository().get_book(id)
        return {"book": book}

    def create_book(self, data):
        with mysql_db.atomic() as transaction:
            try:
                book = BookRepository().create_book(data)
                return {"book": book}
            except Exception as ex:
                transaction.rollback()
                logging.error(ex)
                return ex

    def update_book(self, data):
        book = BookRepository().update_book(data)
        return {"book": book}

    def delete_book(self, id):
        book = BookRepository().delete_book(id)
        return {"book": book}

    def get_book_author(self, query_string):
        author_book = BookRepository().get_book_author(query_string)
        return {"author_book": author_book}
