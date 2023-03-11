from peewee import CompositeKey, ForeignKeyField
from project.repositories.base_repository import BaseRepository
from project.repositories.book_repository import BookRepository
from project.repositories.book_category_repository import BookCategoryRepository


class BookCategoryRepository(BaseRepository):

    category = ForeignKeyField(BookCategoryRepository, backref="category")
    movie = ForeignKeyField(BookRepository, backref="movie")

    class Meta:
        table_name = 'movie_category'
        indexes = (("category", "movie"), True)
        primary_key = CompositeKey("category", "movie")
