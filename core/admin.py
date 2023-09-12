from django.contrib import admin
from core.models import News,Setting,Category,Products,Testimonial,Contact

# Register your models here.

admin.site.register(Setting)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Testimonial)
admin.site.register(Contact)



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display=('title','like','dislike','views','created_at','updated_at')
    search_fields=('title','content')
    list_filter=('created_at','updated_at')
    ordering=('-created_at',)
    readonly_fields=('like','dislike','views','created_at','updated_at')
    fieldsets=(
        (None,{
            'fields':('title','content','image','category','is_active')
        }),
        ('Hide Fields',{
            'fields':('like','dislike','views','created_at','updated_at')
        })
    )


