from django.db import models

class Yozmang(models.Model):
    MAIN_PAGE = models.CharField(max_length=255, verbose_name="Asosiy sahifa")
    SERVICE = models.CharField(max_length=255, verbose_name="Xizmat")
    GET_TT = models.CharField(max_length=255, verbose_name="TT olish")
    PARTNER = models.CharField(max_length=255, verbose_name="Hamkor")
    ORDER = models.BigIntegerField(verbose_name="Buyurtma")

    def __str__(self):
        return self.MAIN_PAGE


class Application(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="To‘liq ism")
    phone = models.CharField(max_length=20, verbose_name="Telefon raqami")
    description = models.TextField(verbose_name="Tavsif")
    product = models.BigIntegerField(verbose_name="Mahsulot")
    status = models.CharField(max_length=50, verbose_name="Holat")

    def __str__(self):
        return self.full_name


class Partner(models.Model):
    image = models.CharField(max_length=255, verbose_name="Rasm")
    url = models.CharField(max_length=255, verbose_name="Havola")
    order = models.IntegerField(verbose_name="Tartib")

    def __str__(self):
        return self.url


class Customers(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="To‘liq ism")
    position = models.CharField(max_length=255, verbose_name="Lavozim")
    image = models.BigIntegerField(verbose_name="Rasm")
    description = models.TextField(verbose_name="Tavsif")

    def __str__(self):
        return self.full_name


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    status = models.CharField(max_length=255, verbose_name="Holat")
    order = models.IntegerField(verbose_name="Tartib")
    image = models.CharField(max_length=255, verbose_name="Rasm")
    short_description = models.TextField(verbose_name="Qisqa tavsif")
    description = models.TextField(verbose_name="Batafsil tavsif")
    brand = models.BigIntegerField(verbose_name="Brend")
    country = models.BigIntegerField(verbose_name="Mamlakat")
    guarantee = models.BigIntegerField(verbose_name="Kafolat")
    category = models.BigIntegerField(verbose_name="Kategoriya")
    is_main_page = models.BooleanField(default=False, verbose_name="Asosiy sahifada")

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.CharField(max_length=255, verbose_name="Rasm")
    product = models.BigIntegerField(verbose_name="Mahsulot")

    def __str__(self):
        return self.image


class ProductCharacteristic(models.Model):
    key = models.CharField(max_length=255, verbose_name="Xususiyat nomi")
    value = models.CharField(max_length=255, verbose_name="Qiymat")
    order = models.BigIntegerField(verbose_name="Tartib")
    product = models.BigIntegerField(verbose_name="Mahsulot")

    def __str__(self):
        return self.key


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nomi")
    icon = models.CharField(max_length=255, verbose_name="Ikonka")
    order = models.IntegerField(verbose_name="Tartib")

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    image = models.BigIntegerField(verbose_name="Rasm")
    date = models.DateField(verbose_name="Sana")
    body = models.TextField(verbose_name="Maqola")

    def __str__(self):
        return self.title
