from project.business.movie_business import MovieBusiness


class MovieService():

    def get_movie(self):
        movie = MovieBusiness().get_movie()
        return {"movie": movie}

    def create_movie(self, data):
        movie = MovieBusiness().create_movie(data)
        return {"movie": movie}

    def update_movie(self, data):
        movie = MovieBusiness().update_movie(data)
        return {"movie": movie}

    def delete_movie(self, data):
        movie = MovieBusiness().delete_movie(data)
        return {"movie": movie}
