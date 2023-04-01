from django.contrib import admin

# Register your models here.
from .models import Banner,category,Brand,color,size,Product,ProductAttribute

admin.site.register(Banner)
admin.site.register(Brand)
admin.site.register(size)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(category,CategoryAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display=('title','color_bg')
admin.site.register(color,ColorAdmin)





class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','brand','color','size','status')
    list_editable=('status',)
admin.site.register(Product,ProductAdmin)


#Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display1=('id','image_tag','Product','price','color','size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)