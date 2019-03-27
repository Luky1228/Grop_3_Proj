from django.shortcuts import render
from .functions import getGraph, drawG
from django.views import generic


# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
        context={},
    )



def GraphV(request):
    if request.method == 'GET':
        y = request.GET['year']
        a = request.GET['graph']
    drawG(getGraph(y, a), y, a)


    return render(
        request,
        'catalog/graphviz.html',
    )

