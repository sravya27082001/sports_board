from django.shortcuts import render
from django.views import generic
from .models import equipments
# Create your views here.

class equipmentsListView(generic.ListView):
    model = equipments

