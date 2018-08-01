from django.db import models
from django.template.defaultfilters import slugify


gender = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)


class SlugMixin(models.Model):

    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(SlugMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Track(SlugMixin):
    name = models.CharField(("Track Name"), max_length=100)
    band = models.ForeignKey("Band", on_delete=models.CASCADE,
                             blank=True, null=True, related_name="tracks")
    album = models.ForeignKey("Album", on_delete=models.CASCADE,
                              blank=True, null=True, related_name="tracks")
    song = models.FileField(upload_to="songs/", max_length=150)
    genre = models.ManyToManyField("Genre")

    def __str__(self):
        return self.name


class Album(SlugMixin):
    name = models.CharField(("Title"), max_length=50)
    prefix = models.CharField(max_length=50)
    asin = models.CharField(("ASIN"), max_length=10)
    band = models.ForeignKey("Band", on_delete=models.CASCADE,
                             blank=True, null=True, related_name="albums")
    label = models.ForeignKey("Label", on_delete=models.CASCADE,
                              blank=True, null=True, related_name="albums")
    cover_image = models.FileField(upload_to="images/", max_length=100)
    release_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Genre(SlugMixin):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=150)
    head_quarters = models.CharField(max_length=50)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Musician(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(
        choices=gender,
        default='male',
        max_length=6
    )
    band = models.ForeignKey("Band", on_delete=models.CASCADE,
                             related_name="musicians")
    instrument = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=50)
    genre = models.ManyToManyField("Genre")
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name
