from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    brand = models.CharField(max_length=150, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    numReviews = models.IntegerField(
        validators=[MinValueValidator(0)], default=0, blank=True
    )
    price = models.DecimalField(
        validators=[MinValueValidator(0.0)],
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
        name="price",
    )
    countInStock = models.IntegerField(
        validators=[MinValueValidator(0)], default=0, name="countInStock"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(0)], null=False, blank=False
    )
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.rating} - {self.product.name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(
        validators=[MinValueValidator(0.0)],
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
    )
    shippingPrice = models.DecimalField(
        validators=[MinValueValidator(0.0)],
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
    )
    totalPrice = models.DecimalField(
        validators=[MinValueValidator(0.0)],
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
    )
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.created_at)


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(
        validators=[MinValueValidator(0.0)],
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.postalCode}, {self.country}"


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    price = models.DecimalField(
        validators=[MinValueValidator(0.0)],
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
    )
    image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.order._id}"
