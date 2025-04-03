from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cat, Toy, Feeding
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

# https://docs.djangoproject.com/en/5.1/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.get_context_data
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


class FeedingCreate(CreateView):
    model = Feeding
    template_name = 'cats/detail.html'
    form_class = FeedingForm

    def form_valid(self, form):
        form.instance.cat = get_object_or_404(Cat, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('cat-detail', kwargs={'pk': self.kwargs['pk']})


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
