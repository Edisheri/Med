

from services.models import Services
from django.db.models import Q

from django.contrib.postgres.search import SearchVector

def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Services.objects.filter(id=int(query))

    return Services.objects.annotate(search=SearchVector('name', 'description')).filter(search=query)



    # keywords = [word for word in query.split() if len(word) > 2]
    #
    #
    # q_objects = Q()
    #
    #
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    #
    # return Services.objects.filter(q_objects)