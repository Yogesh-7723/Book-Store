from django.contrib import admin
from .models import User,Book

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username","email","first_name","last_name","is_active"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name','book_title','price','quantity','stock',"author"]