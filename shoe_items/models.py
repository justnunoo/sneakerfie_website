from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils import timezone
from django.core.validators import MaxValueValidator

# Create your models here.
# class Box(models.Model):
#     img = models.CharField(max_length=100)
#     class Meta:
#         abstract=True



class sub_image(models.Model):
    name = models.CharField(max_length = 100)
    image_path = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Sub images'

    def __str__(self):
        return self.name
    
class ShoeColor(models.Model):
    color = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'shoe colors'

    def __str__(self):
        return self.color

class ShoeSize(models.Model):
    size = models.CharField(max_length = 20)

    class Meta:
        verbose_name_plural = 'shoe sizes'

    def __str__(self):
        return self.size


categories = (
    ('trending', 'trending'),
    ('outdoor', 'outdoor'),
    ('discounted', 'discounted'),
    ('vintage', 'vintage'),
    ('new', 'new')
)

brands = (
    ('jordan', 'jordan'),
    ('nike', 'nike'),
    ('puma', 'puma'),
    ('adidas', 'adidas'),
    ('new_balance', 'new_balance'),
    ('reebok', 'reebok'),
    ('vans', 'vans'),
) 

class Product(models.Model):
    name = models.CharField(max_length=100)
    brands = models.CharField(max_length = 20, choices = brands)
    image_path = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    small_images = models.ManyToManyField(sub_image, blank=True)
    colors = models.ManyToManyField('ShoeColor')
    sizes = models.ManyToManyField('ShoeSize')
    categories = models.CharField(max_length=20, choices = categories)
    discount = models.BooleanField(default=False)
    discount_percent = models.PositiveIntegerField(default = 0, validators=[MaxValueValidator(100)])

    class Meta:
        verbose_name_plural = 'Products'

    @property
    def get_small_images(self):
        return self.small_images.all()
    
    @property
    def get_color(self):
        return self.colors.all()
    
    @property
    def get_size(self):
        return self.sizes.all()
    
    def __str__(self):
        return self.name

#this model is for the cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.ForeignKey(ShoeSize, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(ShoeColor, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)
    price = models.PositiveIntegerField(default = 0)

    class Meta:
        verbose_name_plural = 'Carts'

    def save(self, *args, **kwargs):
        # Call the original save method
        super().save(*args, **kwargs)

        # Update UserProfile cart_count
        user_profile = UserProfile.objects.get_or_create(user=self.user)[0]
        user_profile.cart_count = Cart.objects.filter(user=self.user).aggregate(Sum('quantity'))['quantity__sum'] or 0
        user_profile.save()


    def __str__(self):
        return f"{self.quantity} size {self.size} {self.color}  {self.product.name} added by {self.user.username}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_email = models.OneToOneField(User, on_delete=models.CASCADE)
    cart_count = models.IntegerField(default=0)
    number = models.CharField(max_length=15, blank=True, null=True)  # Add the new 'number' field

    class Meta:
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username
    
    def user_email(self):
        return self.user.email

    def update_cart_count(self):
        # Count the number of unique products in the user's cart
        self.cart_count = Cart.objects.filter(user=self.user).values('product').distinct().count()
        self.save()

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} likes {self.product.name}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.PositiveIntegerField(default = 0)

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order #{self.pk} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places = 2, max_digits = 5)
    quantity = models.PositiveIntegerField(default=1)
    size = models.ForeignKey(ShoeSize, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(ShoeColor, on_delete=models.SET_NULL, null=True, blank=True)
    subtotal = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        # # Calculate the subtotal before saving
        # self.subtotal = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} size {self.size} {self.color} of {self.product.name} in Order #{self.order.pk}"
    

class sales_stats(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity_ordered = models.PositiveIntegerField(default = 0)

    class Meta:
        verbose_name_plural = 'Sales Statistics'

    def __str__(self):
        return f"{self.product} quantity ordered is {self.quantity_ordered}"

    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}"