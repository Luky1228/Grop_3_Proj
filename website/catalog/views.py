from django.shortcuts import render
from .models import GraphCreation, GraphViz
from .functions import getGraph, drowG
from django.views import generic


# Create your views here.
def index(request):


    year = request.GET['year']
    graph = request.GET['graph']
    cr = GraphCreation.objects.all()
    return render(
        request,
        'index.html',
        context={'cr': cr},
    )


class Graphs(generic.ListView):
    model = GraphCreation
