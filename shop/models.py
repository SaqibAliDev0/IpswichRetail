from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)  # Add a default value for stock quantity
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # Make the image field optional
    created_at = models.DateTimeField(auto_now_add=True)  # Track when the product was created
    updated_at = models.DateTimeField(auto_now=True)  # Track when the product was last updated

    def __str__(self):
        return self.name

    def is_in_stock(self):
        """Helper method to check if the product is in stock."""
        return self.stock_quantity > 0
