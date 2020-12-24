from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstview(request):
    context ={
        'sample_var':"ejemplo"

    }
    return render(request,'hookah.html',context)