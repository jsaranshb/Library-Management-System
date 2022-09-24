from django.contrib import admin
from .models import BookCategory, BookDetails

# Register your models here.

admin.site.register(BookCategory)
admin.site.register(BookDetails)