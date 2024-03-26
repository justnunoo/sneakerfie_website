from django.contrib import admin
from .models import Product, sub_image, ShoeColor, ShoeSize, Cart, UserProfile, Cart, Favorite, Order, OrderItem, Message, sales_stats

# Register your models here.
admin.site.register(sub_image)
admin.site.register(ShoeColor)
admin.site.register(ShoeSize)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brands', 'categories', 'discount', 'price']
    list_filter = ['brands', 'categories', 'discount']
admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'size', 'color', 'created_at', 'updated_at']
    list_filter = ['user', 'created_at']
admin.site.register(Cart, CartAdmin)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
    list_filter = ['user']
admin.site.register(Favorite, FavoriteAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'cart_count']
admin.site.register(UserProfile, UserProfileAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price', 'created_at']
    list_filter = ['user', 'created_at']
    inlines = [OrderItemInline]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product']
    list_filter = ['order', 'product']

admin.site.register(OrderItem, OrderItemAdmin)

class Sales_Stats_Admin(admin.ModelAdmin):
    list_display =  ['product', 'quantity_ordered']

admin.site.register(sales_stats, Sales_Stats_Admin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'content', 'timestamp']
    list_filter = ['sender', 'timestamp']

admin.site.register(Message, MessageAdmin)