from django import forms


# class CompanyForm (forms.Form):
#     name = forms.CharField(required=True)
#     tax_number = forms.IntegerField(required=True, label="tax number", initial=0)
from hookah.models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model=Company
        exclude = []