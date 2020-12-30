from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from django.urls.base import reverse_lazy

from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView

from hookah.forms import CompanyForm, HookahForm
from hookah.mixins import AddLoQueSeaMixin
from hookah.models import Hookah, Company


@login_required
def hookah_list_view(request):
    # Almacena la lista de hookas de la base de datos llamando al manager object que nos proporciona django

    # hookah_list_counter = hookah_list.count()
    # print("hookah_list_counter", hookah_list_counter)
    # print("exists?", hookah_list.filter(id=1))
    # print("exists?", hookah_list.filter(id=1).exists())

    # añadir a la base de datos desde la request
    # co = Company.objects.create(name="co",tax_number =5)
    # Hookah.objects.create(name ="broma", company = co)

    # Ordenar la lista
    # print(hookah_list.order_by('name'))

    # filtrar por la foreing key
    # com = Company.objects.get(pk=1)
    # print(hookah_list.filter(company=com))
    # lo mismo pero que empiece por lo que queramos
    # print(hookah_list.filter(company__name__startswith='E'))
    # condicion and
    # print(hookah_list.filter(company__name__startswith='E',abv__gte=5)
    # condicion or IMPORTAR Q
    # print(hookah_list.filter(Q (company__name__startswith='E') | Q (abv__gte=5)))
    # BORRAR
    # Hookah.objects.filter(pk=3).first().delete()
    # sacar inversamente desde la clave foranea
    # com = Company.objects.get(pk=1)
    # print(com.hookah.all())
    # Modificar objetos
    # com = Company.objects.get(pk=1)
    # for hookah in com.hookah.all():
    #     hookah.is_premium = False
    #     # Hay que guardar o hacer commit
    #     hookah.save()

    # print(Hookah.objects.filter(pk__in=[1,2,3,4,5]))

    hookah_list = Hookah.objects.all()
    context = {

        'hookah_list': hookah_list

    }
    return render(request, 'hookah_list.html', context)


@login_required
def hookah_details_view(request, pk):
    # print("usuario", request.user)
    # print("GET", request.GET)
    # print("metodo", request.method)
    # print("preguntar", request.is_ajax())

    context = {
        'hookah': Hookah.objects.get(pk=pk)

    }
    return render(request, 'hookah_details.html', context)


class HookahListView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'hookah_list.html', {
            'hookah_list': Hookah.objects.all()
        })


# CLASES--------------------------------------------------------------

class HookahListViewSecond(LoginRequiredMixin, ListView):
    model = Hookah


class HookahDetailsView(AddLoQueSeaMixin, LoginRequiredMixin, DetailView):
    model = Hookah


class CompanylistView(LoginRequiredMixin, ListView):
    model = Company


class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company

# FORMULARIOS CON DEF----------------------------------------------------
def edit_company_old(request, pk):
    company = get_object_or_404(Company, pk=pk)

    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company.name = form.cleaned_data['name']
            company.tax_number = form.cleaned_data['tax_number']
            company.save()
    else:
        form = CompanyForm(initial={
            'name': company.name,
            'tax_number': company.tax_number,
        })

    context = {
        'form': form

    }

    return render(request, 'company/company_form.html', context)


def edit_company(request, pk):
    company = get_object_or_404(Company, pk=pk)

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            company.save()
    else:
        form = CompanyForm(instance=company)

    context = {
        'form': form

    }

    return render(request, 'company/company_form.html', context)

# FORMULARIOS CON CLASES----------------------------------------------------

class CompanyAndHookahCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "hookah/company_create_with_hookahs.html"
    success_url = reverse_lazy('hookah_list_view')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        if  self.request.POST:
            ctx['hookah_form'] = HookahForm(self.request.POST)
        else:
            ctx['hookah_form'] = HookahForm()
        return ctx

    def form_valid(self, form):
        ctx = self.get_context_data()
        hookah_form = ctx['hookah_form']

        if hookah_form.is_valid():
            self.object = form.save()
            hookah_form.instance = self.company
            hookah_form.save()
        return super().form_valid(form)


class CompanyUpdatedView(UpdateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('hookah_list_view')


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('hookah_list_view')

class HookahCreateView(CreateView):
    model = Hookah
    form_class = HookahForm
    success_url = reverse_lazy('hookah_list_view')

