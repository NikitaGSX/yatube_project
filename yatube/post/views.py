# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    template = 'post/index.html'
    return render(request, template)
#    return HttpResponse(
#        'Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
#        'если у тебя нет правильных <s>вопросов</s> запросов.'
#    )


def group_posts(request, slug):
    template = 'post/group_list.html'
    return render(request, template)
#    return HttpResponse(f'Группа под номером {slug}')
