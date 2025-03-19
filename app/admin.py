from django.contrib import admin
from .models import (
    Yozmang, Application, Partner, Customers, Product,
    ProductImage, ProductCharacteristic, Category, News
)

@admin.register(Yozmang)
class YozmangAdmin(admin.ModelAdmin):
    list_display = ("MAIN_PAGE", "SERVICE", "GET_TT", "PARTNER", "ORDER")
    search_fields = ("MAIN_PAGE",)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "status")
    search_fields = ("full_name", "phone")

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("image", "url", "order")

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "image")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "order", "is_main_page")
    search_fields = ("title", "status")

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("image", "product")

@admin.register(ProductCharacteristic)
class ProductCharacteristicAdmin(admin.ModelAdmin):
    list_display = ("key", "value", "order", "product")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "order")

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    search_fields = ("title", "date")
