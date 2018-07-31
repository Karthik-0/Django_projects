from django.db import models
from django.template.defaultfilters import slugify

gender = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    prefix = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    directors = models.ManyToManyField("Director", verbose_name=("Director"))
    studio = models.ForeignKey("Studio", verbose_name=("Studio"),
                               on_delete=models.CASCADE)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    cover_image = models.URLField(max_length=200)
    review = models.TextField()
    genre = models.ManyToManyField("Genre", verbose_name=("Genre"))
    asin = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)


class Studio(models.Model):
    title = models.CharField(max_length=200)
    prefix = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Studio, self).save(*args, **kwargs)


class Genre(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Genre, self).save(*args, **kwargs)


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    website = models.URLField(max_length=200)
    gender = models.CharField(
        choices=gender,
        default='male',
        max_length=6
    )
