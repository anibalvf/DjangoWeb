from django.contrib import admin

# Register your models here.
from hookah.models import Hookah, Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filer = ('',)
    # exclude = ('',)

admin.site.register(Hookah)
admin.site.register(Company, CompanyAdmin)


