from peewee import CompositeKey, ForeignKeyField
from project.repositories.base_repository import BaseRepository
from project.repositories.book_repository import BookRepository
from project.repositories.category_repository import CategoryRepository


class BookCategoryRepository(BaseRepository):

    category = ForeignKeyField(CategoryRepository, backref="category_id")
    book = ForeignKeyField(BookRepository, backref="book_id")

    class Meta:
        table_name = 'book_category'
        indexes = (("category_id", "book_id"), True)
        primary_key = CompositeKey("category_id", "book_id")
