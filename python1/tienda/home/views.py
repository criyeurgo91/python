from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from .models import *

# Create your views here.
def about_view (request):
    p = Product.objects.first()
    texto= 'Variety Products to best Price!!'
    return render(request, 'about.html', locals())

def team_view (request):
    p = Product.objects.first()
    return render(request, 'team.html',locals())

def contact_view (request):
    p = Product.objects.first()
    info_enviado= False
    email= ''
    tittle= ''
    text= ''
    if request.method == 'POST':
        formulario= contact_form (request.POST)
        if formulario.is_valid ():
            info_enviado = True
            email = formulario.cleaned_data ['email']
            tittle = formulario.cleaned_data ['tittle']
            text = formulario.cleaned_data ['text']
    else:
        formulario = contact_form
    return render(request, 'contact.html', locals())

def product_list_view (request):
    p = Product.objects.first()
    list = Product.objects.filter()
    return render(request,'product_list.html',locals())

def add_product_view (request):
    p = Product.objects.first()
    if request.method == 'POST':
        form = add_product_form(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.status = True
            prod.save()
            form.save_m2m()
            return redirect ('/product_list')
    else:
        form = add_product_form()
    return render(request, 'add_product.html', locals())

def see_product_view(request, id_product):
    p= Product.objects.get(id=id_product)
    return render(request,'see_product.html',locals())

def edit_product_view(request, id_product):
    p = Product.objects.first()
    prod= Product.objects.get(id=id_product)
    if request.method == 'POST':
        form = add_product_form(request.POST, request.FILES, instance=prod)
        if form.is_valid():
            prod= form.save()
            return redirect ('/product_list/')
    else:
        form = add_product_form(instance=prod)
    return render(request, 'edit_product.html', locals())

def delete_product_view(request, id_product):
    p = Product.objects.first()
    prod = Product.objects.get(id=id_product)
    prod.delete()
    return redirect ('/product_list/', locals())



