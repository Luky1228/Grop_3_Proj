from django.shortcuts import render
from .models import GraphCreation, GraphViz
from .functions import getGraph, drowG
from django.views import generic


# Create your views here.
def index(request):
    cr = GraphCreation.objects.all()
    return render(
        request,
        'index.html',
        context={'cr': cr},
    )



def GraphV(request):
    if request.method == 'GET':
        y = request.GET['year']
        a = request.GET['graph']
    drowG(getGraph(y,a))

    # book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'catalog/graphviz.html',
    )

