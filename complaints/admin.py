from django.contrib import admin

from complaints.models import Category, Complaint


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    list_display_links = ('name',)

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'already_raised', 'status', 'created')
    list_editable = ('status',)
    list_filter = ('title', 'category', 'already_raised', 'status', 'created')
    list_display_links = ('title',)