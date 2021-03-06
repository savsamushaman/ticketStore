from django.db import models
from django.shortcuts import reverse

LABEL_CHOICES = (
    ('P', 'success'),
    ('S', 'secondary'),
    ('D', 'danger')
)

CATEGORY_CHOICES = (
    ('T', 'Tickets'),
)

GENRE_CHOICES = (
    ('1', 'Rock'),
    ('2', 'House'),
    ('3', 'Hip-Hop')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    genre = models.CharField(choices=GENRE_CHOICES , default=1, max_length=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })

