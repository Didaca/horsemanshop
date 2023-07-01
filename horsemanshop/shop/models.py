from django.db import models
from django.core import validators


class Category(models.Model):
    MAX_NAME_SYMBOLS = 10

    CATEGORIES_CHOICES = [
        ("rider", "RIDER"),
        ("horse", "HORSE")
    ]

    name = models.CharField(
        max_length=MAX_NAME_SYMBOLS,
        choices=CATEGORIES_CHOICES
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Article(models.Model):

    MAX_LENGTH_NAME = 20
    MAX_LENGTH_CHOICES = 15
    MIN_PRICE_VALUE = 1.00
    ART_IMAGES = "art_images"

    TYPE_CHOICES = [
        ("t-shirt", "T-SHIRT"),
        ("boots", "BOOTS"),
        ("breeches", "BREECHES"),
        ("gloves", "GLOVES"),
        ("saddle cloth", "SADDLE CLOTH"),
        ("bridle", "BRIDLE")
    ]

    SIZES = [
        ("small", "S"),
        ("medium", "M"),
        ("large", "L")
    ]

    COLORS = [
        ("black", "BLACK"),
        ("white", "WHITE"),
        ("grey", "GREY"),
        ("blue", "BLUE"),
        ("pink", "PINK")
    ]

    name = models.CharField(
        max_length=MAX_LENGTH_NAME
    )

    article_type = models.CharField(
        max_length=MAX_LENGTH_CHOICES,
        choices=TYPE_CHOICES
    )

    size = models.CharField(
        max_length=MAX_LENGTH_CHOICES,
        choices=SIZES
    )

    color = models.CharField(
        max_length=MAX_LENGTH_CHOICES,
        choices=COLORS
    )

    image = models.ImageField(
        upload_to=ART_IMAGES
    )

    price = models.FloatField(
        validators=(
            validators.MinValueValidator(MIN_PRICE_VALUE),
        )
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
