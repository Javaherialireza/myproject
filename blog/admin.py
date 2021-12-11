from django.contrib import admin
from .models import * 
class userprofileAdmin(admin.ModelAdmin):
    list_display = ["user" , "avatar" , "description"]
admin.site.register(userprofile , userprofileAdmin)


class articleAdmin(admin.ModelAdmin):
    search_fields = ["title" , "content"]
    list_display = ["title","created_at","category"]

admin.site.register(article , articleAdmin)
#admin.site.register(userprofile)
#admin.site.register(article)
#admin.site.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ["title" , "cover"]
admin.site.register(category,categoryAdmin)
# Register your models here.
