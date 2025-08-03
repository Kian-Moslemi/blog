from django.contrib import admin
from .models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
        'fields':('title','content','slug','image')}),
        ('Status & Author',{   
        'fields':('status','author')}),
        ('Timezone',{
        'fields':('created','edited')}),
    )
    list_display = ('created','author')
    readonly_fields = ('created','edited','slug')
    list_editable = ('author',)
    list_filter = ('status',)
    search_fields = ('title','author__username')
    ordering = ('-created',)


    