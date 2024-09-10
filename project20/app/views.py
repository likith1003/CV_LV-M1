from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
# Create your views here.

def insert_school_by_FBV(request):
    ESFO = School_Form()
    d = {'ESFO': ESFO}
    if request.method == 'POST':
        SFDO = School_Form(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Done')
        return HttpResponse('Invalid Data')
    return render(request, 'insert_school_by_FBV.html', d)


class insert_school_by_CBV(CreateView):
    model = School
    fields = '__all__'
    success_url = 'insert_school_by_cbv'


class school_list(ListView):
    model = School
    context_object_name = 'schools'
    ordering = ['princy']
