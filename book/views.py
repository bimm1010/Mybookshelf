from django.shortcuts import render
from book.models import Product
# Create your views here.


def showoff(request):
    product = Product.objects.all()
    context = {"products": product}
    return render(request, 'book/show.html', context)





