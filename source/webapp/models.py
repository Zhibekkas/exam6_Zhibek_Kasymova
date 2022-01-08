from django.db import models

# Create your models here.

status_choices = [("active","Активно"), ("blocked","Заблокировано")]


class Guest(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Guest name")
    email = models.EmailField(max_length=254, null=False, blank=False, verbose_name="Contact information")
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Content")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    edition_date = models.DateTimeField(auto_now=True, verbose_name="Date of edition")
    status = models.CharField(max_length=200, null=False, verbose_name="process", default="active", choices=status_choices)

    def __str__(self):
        return f"{self.pk}. {self.name}: {self.email}"

    class Meta:
        db_table = 'guests'
        verbose_name = 'guests list'
        verbose_name_plural = 'guest book list'
