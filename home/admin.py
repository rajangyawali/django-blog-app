from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from . models import Author, BlogPost, Search, Contact

# Register your models here.

class BlogPostModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["title", "description","category", "author",  "posted"]
    list_display_links = ["description", "category", "author"]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ["category", "author", "posted"]
    
    class Meta:
        model = BlogPost

admin.site.register(Author)
admin.site.register(Search)
admin.site.register(Contact)
admin.site.register(BlogPost, BlogPostModelAdmin)


