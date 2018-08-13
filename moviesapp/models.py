from django.db import models


class Movies(models.Model):
    title = models.TextField()
    year = models.TextField()
    rated = models.TextField()
    released = models.TextField()
    runtime = models.TextField()
    genre = models.TextField()
    director = models.TextField()
    writer = models.TextField()
    actors = models.TextField()
    plot = models.TextField()
    language = models.TextField()
    country = models.TextField()
    awards = models.TextField()
    poster = models.TextField()
    ratings = models.TextField()
    metascore = models.TextField()
    imdb_rating = models.TextField()
    imdb_votes = models.TextField()
    imdb_id = models.TextField()
    type = models.TextField()
    dvd = models.TextField()
    boxoffice = models.TextField()
    production = models.TextField()
    website = models.TextField()
    response = models.TextField()

    def year_dir(self):
        return 'Movie ' + self.title + ' was made in ' + self.year + ' by ' + self.director

    def __str__(self):
        return self.title


class Comments(models.Model):
    commented_movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    comment = models.TextField()


class Add(models.Model):
    add = models.TextField()
