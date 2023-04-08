from django.shortcuts import render
from .models import Inventar
from django.db.models import Q

def MyView(request):
    search_post = request.GET.get('search')

    if search_post:
        posts = Inventar.objects.filter(Q(name__icontains=search_post))
        
    else:
        posts = Inventar.objects.all()

   

    return render(request, "list.html", {"query_results":posts})


# Create your views here.
