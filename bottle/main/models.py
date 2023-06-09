from django.db import models
from django.utils.html import mark_safe

#Banner
class Banner(models.Model):
    img=models.CharField(max_length=200)
    alt_text=models.CharField(max_length=300)

    class Meta:
        verbose_name_plural='1. Banners'




# Category
class category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_imgs/")
    
    class Meta:
        verbose_name_plural='2. Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))      

    def __str__(self):
        return self.title




#brand

class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="brand_imgs/")
    
    class Meta:
        verbose_name_plural='3. Brands'


    def __str__(self):
        return self.title



#color

class color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='4. colors'

    def color_bg(self):
        return mark_safe('<div style="width:50px; height:50px; background-color:%s"></div>' % (self.color_code))


    def __str__(self):
        return self.title




#size      


class size(models.Model):
    title=models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='5. Sizes'
    
 
    def __str__(self):
        return self.title





#product model

class Product(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="product_imgs/")
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    specs=models.TextField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color=models.ForeignKey(color,on_delete=models.CASCADE)
    size=models.ForeignKey(size,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural='6. Products'






def __str__(self):
    return self.title

#Product Attribute 
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(color,on_delete=models.CASCADE)
    size=models.ForeignKey(size,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    
    class Meta:
        verbose_name_plural='7. ProductAttributes'




    def __str__(self):
        return self.product.title