from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat, Breed
# Create your views here.

class CatList(LoginRequiredMixin, View):
    def get(self, request):
        bc = Breed.objects.all().count()
        cl = Cat.objects.all()

        ctx = {'breed_count': bc, 'cat_list': cl}
        return render(request, 'cats/cat_list.html', ctx) 

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Breed.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'cats/make_list.html', ctx)

# Cat views
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

# Breed views
class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

