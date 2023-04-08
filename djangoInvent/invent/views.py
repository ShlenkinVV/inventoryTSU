from django.shortcuts import render
from .models import Inventar
from django.db.models import Q

def MyView(request):
    search_post = request.GET.get('search')

    if search_post:
        posts = Inventar.objects.filter(Q(name__icontains=search_post))
        
    else:
        posts = Inventar.objects.all()

    #fields = [f for f in table._meta.fields]
    #queries = [Q(**{f.name: SEARCH_TERM}) for f in fields]


   # qs= Q()
    #for query in queries:
   #     qs = qs | query


   # query_results = Inventar.objects(posts)
    # for q in query_results :
    #     print(q.name, q.num, q.num_kab, )

    return render(request, "list.html", {"query_results":posts})


# Create your views here.
