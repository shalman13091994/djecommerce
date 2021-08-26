from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name=models.CharField(max_length=255, db_index=True)
    slug=models.SlugField(max_length=255, unique=True)

    class Meta:
        #django add s to the category example categorys so we use verbose
        verbose_name_plural ='Categories'

    # when we click on the title i.e., django, react it will go the detail page
    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug]) #category list is pattern name

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    #who created the product
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.jpg' ) #install pillow
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True) #whether product is on stock
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
# django add s to the product example products so we use verbose
        verbose_name_plural = 'Products'
#last time added in the database in the first (descending order)
        ordering = ('-created',) #it should be tuple addded comma

# when we click on the title i.e., django, react it will go the detail page

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
        #self.slug = whatever item is currently wants to view

    def __str__(self):
        return self.title
