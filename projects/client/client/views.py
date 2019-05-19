from django.http import HttpResponse, JsonResponse
from django.template import loader

#our view which is a function named ind
from django.shortcuts import render, redirect  
from .forms import ServicesForm, ProductsForm
from .models import Services,Products

def index(request):
    template = loader.get_template('client/index.html')
    context = ["Gopal",27]
    return HttpResponse(template.render({"data":context},request))

def admin(request):
    template = loader.get_template('client/admin.html')
    context = {}
    return HttpResponse(template.render(context,request))

def login(request):
    template = loader.get_template('client/login.html')
    context = {}
    return HttpResponse(template.render(context,request))

def service(request):
    template = loader.get_template('client/services.html')
    context = ["Gopal",27]
    return HttpResponse(template.render({"data":context},request))

def team(request):
    template = loader.get_template('client/team.html')
    context = ["Gopal",27]
    return HttpResponse(template.render({"data":context},request))

def portfolio(request):
    template = loader.get_template('client/portfolio.html')
    context = ["Gopal",27]
    return HttpResponse(template.render({"data":context},request))

def createService(request):
    if request.method == "POST":  
        form = ServicesForm(request.POST)
        if form.is_valid(): 
            try:   
                form.save() 
                return redirect('/services')  
            except:  
                pass  
    else:  
        form = ServicesForm() 

    template = loader.get_template('client/services.html')
    context = ["Gopal",27]
    return HttpResponse(template.render({"data":context},request))

def listProducts(request):
    products = Products.objects.all()
    template = loader.get_template('client/admin/product/list.html')
    #rendering the template in HttpResponse
    return HttpResponse(template.render({"products":products},request))

def createProduct(request):
    if request.method == "POST":  
        form = ProductsForm(request.POST,request.FILES)
        if form.is_valid(): 
            try:   
                form.save() 
                return redirect('/')  
            except:  
                pass  
    else:  
        form = ProductsForm() 

    template = loader.get_template('client/admin/product/create.html')
    context = ["Gopal",27]
    return HttpResponse(template.render({"form":form},request))

def viewProduct(request,id):
    product = Products.objects.get(id=id)
    template = loader.get_template('client/admin/product/view.html')
    #rendering the template in HttpResponse
    return HttpResponse(template.render({"product":product},request))

def deleteProduct(request,id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('/list/')

def editProduct(request,id):
    product = Products.objects.get(id=id) 
    if request.method == "POST":  
        form = ProductsForm(request.POST,request.FILES, instance = product)
        if form.is_valid(): 
            try:   
                form.save() 
                return redirect('/list')  
            except:  
                pass  
    else:  
        form = ProductsForm() 

    template = loader.get_template('client/admin/product/edit.html')
    context = ["Gopal",27]
    return HttpResponse(template.render({"product":product},request))