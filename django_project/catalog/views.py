from django.http import HttpResponse

def catalog(request):
    return HttpResponse('<h1>Каталог</h1><p>Здесь будут отображаться товары.</p><a href="/cart/">Перейти в корзину</a>')