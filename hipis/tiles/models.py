from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=15)
    hexcolor = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=15)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tile(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateField(editable=False, auto_now=True)

    def __str__(self):
        return self.name
