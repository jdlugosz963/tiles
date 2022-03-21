from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=15)
    color = models.CharField(
        max_length=15,
        choices = (
            ('bg-red-600', 'Red'),
            ('bg-green-600', 'Blue'),
            ('bg-lime-600', 'Lime'),
            ('bg-emerald-600', 'Emerald'),
            ('bg-indigo-600', 'Indigo'),
            ('bg-violet-600', 'Violet'),
            ('bg-rose-600', 'Rose')
        ),
        default = 'Lime'
    )

    def __str__(self):
        return self.name

class Tile(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateField(editable=False, auto_now=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.owner
