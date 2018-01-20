from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from dyplomowanie.model.Deklaracja import DeclarationForm
from .forms import OptionsForm, DeclarationForm2
from dyplomowanie.model.Temat import Temat
from dyplomowanie.DTO.tematy import TematDTO


class Base(View):
    def get(self, request):
        context = {'user': 'Jan Kowalski'}
        return render(request, 'base.html', context)


class Work(View):
    def get(self, request):
        context = {'user': 'Jan Kowalski'}
        return render(request, 'moja_praca.html', context)







