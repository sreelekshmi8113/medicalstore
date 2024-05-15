from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from .models import Product

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
 






def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            # Redirect to login page after successful signup
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login 

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Redirect to home page after successful login
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



#create
from django.shortcuts import render, redirect
from .forms import ProductForm
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})



from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
#read
@login_required(login_url='/login/')
def product_read(request):
    
    product_list=Product.objects.all()
    return render(request,'home.html',{'product_list':product_list})

#update
def product_update(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})

#delete
def product_delete(request,pk):
    value=Product.objects.get(pk=pk)  
    if request.method == 'POST':
        value.delete()
        return redirect('home')
    
    return render(request,'home.html',{'value': value})

#logout
from django.contrib.auth import logout

@login_required(login_url='/login/')
def logout_view(request):
        logout(request)
        return redirect('signup')

#search
# def search(request):
#     if 'q' in request.GET:
#         q=request.GET[q]
#         data=Product.objects.filter(name__icontains=q)
#     else:
#         data=Product.objects.all()
#         context={'data':data}
#     return render (request,'home.html',context)

# views.py

# from django.shortcuts import render
# from .models import Product

# def search(request):
#     query = request.GET.get('q')
#     results = []
#     if query:
#         results = Product.objects.filter(title__icontains=query)
#     return render(request, 'home.html', {'results': results, 'query': query})

from django.shortcuts import render
from .models import Product  # Assuming Product is your model

def search(request):
    sea=request.GET.get('q','')
    if sea:
        product_list=Product.objects.filter(name__istartswith=sea)
    else:
        product_list = Product.objects.all()

    return render(request, 'home.html', {'product_list': product_list, 'search_query':sea})
    # context = {}
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     data = Product.objects.filter(name__icontains=q)
    # else:
    #     data = Product.objects.all()
    # context['data'] = data
    # return render(request, 'home.html', context)

    
