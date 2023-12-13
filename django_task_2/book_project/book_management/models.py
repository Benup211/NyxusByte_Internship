from django.db import models

# Create your models here.
class Author(models.Model):
    auth_name=models.CharField(max_length=50)
    auth_bio=models.TextField()
    class Meta:
        ordering=['auth_name']
        verbose_name="Author Details"
        verbose_name_plural="All Registered Author Detail"
    def __str__(self):
        return self.auth_name
class Book(models.Model):
    book_title=models.CharField(max_length=50)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="book")
    pub_date=models.DateField()
    class Meta:
        # db_table_comment="Book Entry"
        verbose_name="Single Book Details"
        verbose_name_plural="All Registered Book Detail"

    def __str__(self):
        return self.book_title