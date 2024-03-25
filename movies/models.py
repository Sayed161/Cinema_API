from django.db import models
from autoslug import AutoSlugField

Status = (
    ('coming_up','Coming Up'),
    ('starting','Starting'),
    ('running','Running'),
    ('finished','Finished'),
)

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    protagonist = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='media')
    trailer = models.URLField()
    start_date = models.DateTimeField()
    status = models.CharField(max_length=200,choices = Status,default='coming_up')
    ranking = models.IntegerField(default=0)
    slug = AutoSlugField(populate_from = 'name',null=True)

    def __str__(self):
        return self.name