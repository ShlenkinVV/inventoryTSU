from django.shortcuts import render
from .models import Inventar

def MyView(request):
    
    query_results = Inventar.objects.all()
    # for q in query_results :
    #     print(q.name, q.num, q.num_kab, )

    return render(request, 'templates\list.html', context=query_results)


# Create your views here.
