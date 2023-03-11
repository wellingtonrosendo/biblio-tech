
from peewee import AutoField, CharField, DateField
from project.repositories.base_repository import BaseRepository
from playhouse.shortcuts import dict_to_model, model_to_dict


class BookRepository(BaseRepository):

    id = AutoField()
    name = CharField()
    release_date = DateField()

    class Meta:
        table_name = 'book'

    def get_book(self):
        book = list(BookRepository().select().dicts())
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
