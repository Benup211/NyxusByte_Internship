from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
class Genre(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    price=models.IntegerField()
    description=models.TextField()
    book_image=models.ImageField()
    def __str__(self) -> str:
        return self.title