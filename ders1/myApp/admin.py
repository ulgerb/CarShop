from django.contrib import admin
from myApp.models import *
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ['title','new_date','id',]
class ShopAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'adet', 'fiyat', 'id', ]


admin.site.register(Post,PostAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(UserSave)
