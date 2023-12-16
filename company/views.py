from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Companie, Catagory
from researcher.models import Product


# Create your views here.
@login_required(login_url='signin')
def home(request):
    products = Product.objects.order_by('-date')
    if request.user.username != 'researcher':
        user_profile = Companie.objects.get(user=request.user)
        product_obj = Product.objects.filter(company_name=user_profile.companiesName)
        return render(request, 'home.html', {'products': products, 'product_obj': product_obj, 'companie_obj': user_profile})
    else:
         product_obj = Product.objects.all()
         return render(request, 'index.html', {'products': products, 'product_obj': product_obj})


def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
  

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                print(user_model.username)
                
                if user_model.username != 'researcher':
                    new_companie = Companie.objects.create(user=user_model, id_user=user_model.id)
                    new_companie.save()
                    return redirect('company')

                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')
    else:
        return render(request, 'SignUp_Page.html')
    

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credential is Invalid')
            return redirect('signin')
    else:        
        return render(request, 'Signin_Page.html')    
    

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')      

@login_required(login_url='signin')
def company(request):
    companie_obj = Companie.objects.get(user=request.user)
    catagories = Catagory.objects.all()
    
    if request.method == 'POST':
        companiesName = request.POST['companiesName']
        categorie_pk = request.POST.get('category')
        phonenumber = request.POST['phonenumber']
        location = request.POST['location']
        website = request.POST['website']
        categorie = Catagory.objects.get(pk=categorie_pk)
        

        companie_obj.companiesName = companiesName
        companie_obj.categorie = categorie
        companie_obj.phonenumber = phonenumber
        companie_obj.location = location
        companie_obj.website = website
        companie_obj.save()
        return redirect('/')
    return render(request, 'companies_info.html', {'companie_obj': companie_obj, 'catagories':catagories})
     

@login_required(login_url='signin')
def response(request, pk):
    product_obj = Product.objects.get(product_id=pk)
        
    if request.method == 'POST':
        price = request.POST['price']
        total = request.POST['total']
        availability = request.POST.get('availability')
        remark = request.POST['remark']
        
        product_obj.price = price
        product_obj.total = total
        product_obj.availability = availability
        product_obj.remark = remark
        
        product_obj.save()
        return redirect('research')
    return render(request, 'response.html', {'product': product_obj})


@login_required(login_url='signin')
def update_response(request, pk):
    product_obj = Product.objects.get(product_id=pk)
        
    if request.method == 'POST':
        price = request.POST['price']
        total = request.POST['total']
        availability = request.POST.get('availability')
        remark = request.POST['remark']
        
        product_obj.price = price
        product_obj.total = total
        product_obj.availability = availability
        product_obj.remark = remark
        
        product_obj.save()
        return redirect('research')
    return render(request, 'update_user_response.html', {'product': product_obj})

def index(request):
    return render(request, 'main_company.html')

def companyinfo(request):
    return render(request, 'companyinfo.html')

def agree(request):
    return render(request, 'agree.html')

   