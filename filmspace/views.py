from django.shortcuts import render
from .models import Articles
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
# Create your views here.
peopleNum = 0


def index(request):
    global peopleNum
    peopleNum += 1
    articles = get_list_or_404(Articles)[:15]
    return render(request, 'filmspace/index.html', {'articles': articles,'peopleNum': peopleNum})


def getfilminfo(request, film_id):
    global peopleNum
    peopleNum += 1
    article = get_object_or_404(Articles, pk=film_id)
    filmshow = {
        'article': article,
        'peopleNum': peopleNum
    }
    return render(request, 'filmspace/filminfo.html', filmshow)