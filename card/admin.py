from django.contrib import admin
from .models import Cards, Category

# Register your models here.


class CardAdmin(admin.ModelAdmin):
    list_display = ('text', 'translate', 'slug',)
    prepopulated_fields = {'slug': ('text',)}

admin.site.register(Cards, CardAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
