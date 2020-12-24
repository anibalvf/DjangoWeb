from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstview(request):
    context ={
        'sample_var':"ejemplo",
        'sample_dario':[1,4,5,6]

    }
    return render(request,'hookah.html',context)