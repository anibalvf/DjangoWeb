from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


# class CompanyForm (forms.Form):
#     name = forms.CharField(required=True)
#     tax_number = forms.IntegerField(required=True, label="tax number", initial=0)
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory

from hookah.models import Company, Hookah


class CompanyForm(forms.ModelForm):

    class Meta:
        model=Company
        exclude = []

    # Crispy forms
    def __init__(self,*args,**kwargs):

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'company-form'
        self.helper.form_class = 'blue'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit-name', 'Guardar'))


    # clean de cada campo
    def clean_name(self):
        name = self.cleaned_data['name']
        if name == "anibal":
            raise ValidationError("Jamas",code="invalid")
        return name

    # clean de cada campo
    def clean_tax_number(self):
        tax = self.cleaned_data['tax_number']
        if tax == 0:
            raise ValidationError("no puedes",code="invalid")
        return tax

    # clean de todos los datos del formulario
    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data.get('name')
        tax = self.cleaned_data.get('tax_number')

        if name == "pepe" and tax < 3:
            # error global
            raise ValidationError("DANGER", code="invalid")
            # error especifico
            # self.add_error('tax_number', "muy mal")

class HookahForm(forms.ModelForm):

    class Meta:
        model=Hookah
        exclude = []


# Formsets
HookahFormset = inlineformset_factory(Company,Hookah,form=HookahForm, extra = 2)

