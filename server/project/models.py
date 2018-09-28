from django.db import models


class Category(models.Model):

    name = models.CharField(
        verbose_name='name category',
        max_length=250,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    modified = models.DateTimeField(
        auto_now=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(
        verbose_name='name product',
        max_length=100,
        unique=True
    )

    image = models.ImageField(
        upload_to='products_images',
        blank=True
    )

    short_desc = models.CharField(
        verbose_name='кратко', 
        max_length=100, 
        blank=True
    )

    description = models.TextField(
        verbose_name='подробно',
        blank=True
    )

    price = models.DecimalField(
        verbose_name='цена', 
        max_digits=12,
        decimal_places=2,
        default=0
    )

    discount = models.DecimalField(
        verbose_name='discount', 
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='склад',
        default=0,
    )

    def __str__(self):
        return self.name
