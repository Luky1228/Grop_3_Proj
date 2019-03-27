from django.shortcuts import render
from .models import GraphCreation, GraphViz
from django.views import generic


# Create your views here.
def index(request):
    cr = GraphCreation.objects.all()
    return render(
        request,
        'index.html',
        context={'cr': cr},
    )


class Graphs(generic.ListView):
    model = GraphCreation
