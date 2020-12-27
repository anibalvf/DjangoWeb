from django.db import models
from hookah.utils import image_upload_location

# Create your models here.

class Company (models.Model):
    name = models.CharField("Name",max_length = 50)
    tax_number = models.IntegerField("Tax number", unique=True)

class Hookah(models.Model):
    COLOR_YELLOW = 1
    COLOR_BLACK = 2
    COLOR_WHITE = 3
    COLOR_CHOICES = (
        (COLOR_YELLOW ,"yellow"),
        (COLOR_BLACK,"black"),
        (COLOR_WHITE,"white"),
    )

    # CAMPO TIPO STRING CON MAXIMO DE 50
    name = models.CharField("Name",max_length = 50)
    price = models.DecimalField("Price", max_digits=5, decimal_places=2,default = 0)
    is_premium = models.BooleanField("Is Premium?",default=False)
    # CAMPO DE ELECCION DENTRO DE UNA LISTA DEFINIDA CON VARIABLES FINALES ARRIBA
    color = models.PositiveSmallIntegerField("Color",choices = COLOR_CHOICES,default = COLOR_BLACK)
    # CAMPO TIPO IMAGEN QUE SE PUEDE QUEDAR EN NULL Y EN BLACK ( NO SON LO MISMO)
    image = models.ImageField("image",blank = True,null = True, upload_to = image_upload_location)

    # CAMPO PARA DEFINIR UNA CLAVE FORANEA
    company = models.ForeignKey(Company,related_name="hookah",on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Hookah"
        verbose_name_plural = "Hookahs"
        ordering = ['-name']
    def __str__(self):
        return self.name    


class country(models.Model):
    name = models.CharField("Name",max_length = 50)
    # CAMPO PARA DEFINIR UNA RELACION MUCHOS A MUCHOS CLAVE FORANEA
    hookah = models.ManyToManyField(Hookah,blank = True, related_name="Country")


