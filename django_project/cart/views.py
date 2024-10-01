from django.http import HttpResponse

def cart(request):
    return HttpResponse('<h1>Корзина</h1><p>Здесь будут отображаться добавленные товары.</p><a href="/">Перейти на главную</a>')