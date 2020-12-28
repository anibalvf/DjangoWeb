from django.db import models


class Shop (models.Models):
    name = models.CharField("Name",max_length=200)