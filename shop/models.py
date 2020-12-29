from django.db import models


class Shop (models.Model):
    name = models.CharField("Name",max_length=200)
