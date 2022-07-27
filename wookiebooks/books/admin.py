from django.contrib import admin
from .models import User, Book

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'author_pseudonym', 'email']
    ordering = ['author_pseudonym']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_name', 'price']
    ordering = ['title']

    def get_name(self, obj):
        return obj.author.author_pseudonym

    get_name.admin_order_field = 'author'
    get_name.short_description = 'Author Pseudonym'

admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)