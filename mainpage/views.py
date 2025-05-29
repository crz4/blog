# товар/views.py
from django.shortcuts import render
from .models import Товар

def список_товаров(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    товары = Товар.objects.all()
    
    if min_price:
        товары = товары.filter(цена__gte=min_price)
        
    if max_price:
        товары = товары.filter(цена__lte=max_price)
        
    context = {
        'товары': товары,
        'request': request,
    }
    
    return render(request, 'товар/list.html', context)