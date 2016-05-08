from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView, FormView

from .models import Collection


class IndexView(generic.ListView):
    template_name = 'library/index.html'
    context_object_name = 'collection'

    def get_queryset(self):
        """Return the last five published questions."""
        return Collection.objects.order_by('-date_created')


class DetailView(generic.DetailView):
    model = Collection
    template_name = 'library/detail.html'

class CollectionCreate(CreateView):
    model = Collection
    fields = ['name']
    success_url = "/library"