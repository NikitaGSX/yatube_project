# posts/views.py
from django.shortcuts import render
# Импортируем модель, чтобы обратиться к ней
from .models import Post


def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = 'posts/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Последние обновления на сайте'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'title': title,
        'posts': posts,
        'text': 'Это главная страница проекта Yatube',
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Социальная сеть для авторов'
    # Словарь с данными принято называть context
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context)
