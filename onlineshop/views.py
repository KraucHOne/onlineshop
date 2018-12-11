from django.shortcuts import render

# Create your views here.

def goods_list(request):
    return render(request, 'onlineshop/goods_list.html', {})
