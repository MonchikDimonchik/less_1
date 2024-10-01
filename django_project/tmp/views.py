from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Главная страница</h1><a href="/catalog/">Перейти в каталог</a>')