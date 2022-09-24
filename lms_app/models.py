from django.db import models

# Create your models here.

# Model of the cateories of books.
class BookCategory(models.Model):
    Category_name = models.CharField(max_length=20)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.Category_name

# Model of book details.
class BookDetails(models.Model):
    book_category = models.ForeignKey(BookCategory,on_delete=models.CASCADE,related_name="category")
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    edition = models.CharField(max_length=6)
    quantity = models.IntegerField()  

    def __str__(self)-> str:
        return self.name
