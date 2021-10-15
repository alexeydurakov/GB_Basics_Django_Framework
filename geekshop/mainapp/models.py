from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='имя',
        unique=True,
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name