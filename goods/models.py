from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Category Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Product Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Image')
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=7, verbose_name='Price')
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=4, verbose_name='Discount in %')
    quantity = models.IntegerField(default=0, verbose_name='Quantity')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Category')

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
