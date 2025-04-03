from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cat, Toy
from .forms import FeedingForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


class CatList(ListView):
    model = Cat
    template_name = 'cats/index.html'


class CatDetail(DetailView):
    model = Cat
    template_name = 'cats/detail.html'
    feeding_form = FeedingForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feeding_form'] = self.feeding_form
        return context


class CatCreate(CreateView):
    model = Cat
    fields = '__all__'


class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']


class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'


def add_feeding(request, pk):
    form = FeedingForm(request.POST)

    if form.is_valid():

        new_feeding = form.save(commit=False)
        new_feeding.cat_id = pk
        new_feeding.save()
    return redirect('cat-detail', pk=pk)


class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'


class ToyList(ListView):
    model = Toy


class ToyDetail(DetailView):
    model = Toy


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'
