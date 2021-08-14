from django.db import models
# from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.
class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField(max_length=255, db_index=True)
    slug = models.CharField(max_length=255, unique=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    # def get_absolute_url(self):
    #     return reverse("store:category_list", args=[self.slug])
    
    def __str__(self):
        """Unicode representation of Category."""
        return self.name

class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_creator")
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="admin")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    slug = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField()
    is_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True,)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        """Unicode representation of Product."""
        return self.title
