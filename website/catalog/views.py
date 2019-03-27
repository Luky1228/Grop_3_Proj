from django.shortcuts import render
from .functions import getGraph, drawG
from django.views import generic

Y = 2015
GT = 'co-authorship'
LO = 'random'
# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
        context={},
    )



def GraphV(request):
    if request.method == 'GET':

        if 'year' in request.GET.keys():
            global Y
            Y = request.GET['year']
        if 'graph' in request.GET.keys():
            global GT
            GT = request.GET['graph']
        if 'layout' in request.GET.keys():
            global LO
            LO = request.GET['layout']
        year = Y
        Gtype = GT
        layout = LO
    drawG(getGraph(year, Gtype), year, Gtype, layout)


    return render(
        request,
        'catalog/graphviz.html',
    )

