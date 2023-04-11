
from peewee import ForeignKeyField, CharField, DateField, fn, JOIN
from project.repositories.base_repository import BaseRepository
from project.repositories.author_repository import AuthorRepository
from playhouse.shortcuts import dict_to_model, model_to_dict


class BookRepository(BaseRepository):

    id = CharField()
    name = CharField()
    author_id = ForeignKeyField(
        AuthorRepository, related_name="author_id")
    release_date = DateField()
    created_at = DateField()
    updated_at = DateField()
    deleted_at = DateField()

    class Meta:
        table_name = 'book'

    def list_book(self):
        book = list(BookRepository().select().dicts())
        return book

    def get_book(self, id):
        book = BookRepository().select().where(
            BookRepository.id == id).dicts().first()
        return book

    def create_book(self, data):
        try:
            book = BookRepository().create(data)
            return {"sucesso": "Livro cadastrado com suvesso", "livro": book}
        except Exception as ex:
            return {"erro": "Erro ao cadastrar", "status": ex}

    def update_book(self, book, data):
        book_dict = model_to_dict(book)
        try:
            for key in data.keys():
                book_dict[key] = data[key]
            book = dict_to_model(BookRepository, book_dict)
            book.save()
            return {"sucesso": "Livro arualizado com suvesso", "livro": book}
        except Exception as ex:
            return {"erro": "Erro ao atualizar", "status": ex}

    def delete_book(self, data):
        return {}

    def get_book_author(self, query_string=None, page=1, perpage=20):
        __where = True

        if query_string:
            __where = BookRepository.name.contains(query_string)

        author_list = list(
            BookRepository().select(
                AuthorRepository.name.alias("author"),
                BookRepository.name.alias("book"),
                fn.CONCAT(AuthorRepository.id, BookRepository.id)
            ).join(
                AuthorRepository,
                on=(BookRepository.author_id == AuthorRepository.id)
            ).where(__where).dicts()
        )
        return author_list
