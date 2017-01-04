from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse

from subprocuraduria.models import Subprocuraduria, Direccion


class CreateSubprocuraduriaView(CreateView):
    model = Subprocuraduria
    fields = '__all__'
    template_name = 'subprocuradurias/subprocuraduria_form.html'
    success_url = reverse_lazy('listado_subprocuradurias')

    def get_context_data(self, **kwargs):
        context = super(CreateSubprocuraduriaView, self).get_context_data(**kwargs)
        return context


class EditSubprocuraduriaView(UpdateView):
    model = Subprocuraduria
    fields = '__all__'
    template_name = 'subprocuradurias/subprocuraduria_form.html'
    success_url = reverse_lazy('listado_subprocuradurias')


class SubprocuraduriaListView(ListView):
    model = Subprocuraduria
    paginate_by = 50
    template_name = 'subprocuradurias/listado_subprocuradurias.html'

    def get_context_data(self, **kwargs):
        context = super(SubprocuraduriaListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        queryset = Subprocuraduria.objects.all().order_by('-id')
        return queryset


class CreateDireccionView(CreateView):
    model = Direccion
    fields = '__all__'
    template_name = 'subprocuradurias/direccion_form.html'
    success_url = reverse_lazy('listado_direcciones')

    def get_context_data(self, **kwargs):
        context = super(CreateDireccionView, self).get_context_data(**kwargs)
        return context


class DireccionListView(ListView):
    model = Direccion
    paginate_by = 50
    template_name = 'subprocuradurias/listado_direcciones.html'

    def get_context_data(self, **kwargs):
        context = super(DireccionListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        queryset = Direccion.objects.all().order_by('-id')
        return queryset

