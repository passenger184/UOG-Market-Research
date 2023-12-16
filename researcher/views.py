from django.shortcuts import render, redirect
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.mail import send_mail
from .models import Product, Unit
from company.models import Companie, Catagory


# Create your views here.
def send_request_email(request, company_name, product_name):
    companies = Companie.objects.get(companiesName=company_name)
    sent_email = companies.user.email

    mes = f"""Dear {company_name},

        I hope this email finds you well. I am writing on behalf of UOG Market Research group and we are interested in conducting market research. As a part of our research, we would like to request pricing information for {product_name}.

        Could you please provide us with the pricing details by filling out the attached form on our website: http://127.0.0.1:8000/research We would appreciate it if you could answer us as soon as possible.

        Thank you for your time and consideration.

        Best regards,
        UOG Market Research
        """
    subject = f'Request for {product_name}'
    message = mes
    from_email = 'Hussenjebril12@gmail.com'
    recipient_list = [sent_email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=True)
        
@login_required(login_url='signin')
def request(request):
    catagories = Catagory.objects.all()
    units = Unit.objects.all()
    if request.method == 'POST':
        categorie_pk = request.POST.get('category')
        categorie = Catagory.objects.get(pk=categorie_pk)
        companies = Companie.objects.filter(categorie=categorie)
        for category in companies:
            company_name = category.companiesName
            product_name = request.POST['product_name']
            quantity = request.POST['quantity']
            description = request.POST['description']
            unit_pk = request.POST.get('unit')
            quantity = request.POST['quantity']
            remark = request.POST['remark']
            unit = Unit.objects.get(pk=unit_pk)
        
            product = Product()
            product.company_name = company_name
            product.product_name = product_name
            product.quantity = quantity
            product.description = description
            product.unit = unit
            product.remark = remark
            product.save()

            send_request_email(request, company_name, product_name)
        return redirect('research')
    return render(request, 'request.html', {'catagories': catagories, 'units': units})


@login_required(login_url='signin')
def research(request):
    products = Product.objects.order_by('-date')
    company_count = Companie.objects.count()
    requested_count = Product.objects.filter(status='pending').count()
    responded_count = Product.objects.filter(status='responded').count()
    total_requested_count = requested_count + responded_count
    context = {
        'products': products,
        'company_count': company_count,
        'total_requested_count': total_requested_count,
        'responded_count': responded_count
        }
    if(request.user.username == 'researcher'):
        return render(request, 'market_research.html', context)
    else:
        user_profile = Companie.objects.get(user=request.user)
        product_profile = Product.objects.filter(company_name=user_profile.companiesName).order_by('-date')
        if product_profile.count() == 0:
            product_profile = False
        return render(request, 'market_research_user.html', { 'product_profile': product_profile})


@login_required(login_url='signin')
def search(request):
    today = date.today()
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)
    last_year = today - timedelta(days=365)

    products = Product.objects.order_by('-date')
    query = request.GET.get('search-input')
    status = request.GET.get('status')
    date_filter = request.GET.get('date')

    
    if query != '' and query is not None:
        products = products.filter(Q(company_name__icontains=query)).order_by('-date')
    
    if status != '' and status is not None:
        products = products.filter(Q(status__icontains=status)).order_by('-date')
    else:
        status = 'All'    
    
    if date_filter == 'today':
        products = products.filter(date__date=today)
    elif date_filter == 'yesterday':
        products = products.filter(date__date=today - timedelta(days=1))
    elif date_filter == 'this-week':
        products = products.filter(date__date__gte=last_week)
    elif date_filter == 'last-week':
        products = products.filter(date__date__lt=last_week, date__date__gte=last_week - timedelta(days=7))
    elif date_filter == 'this-month':
        products = products.filter(date__date__gte=last_month)
    elif date_filter == 'last-month':
        products = products.filter(date__date__lt=last_month, date__date__gte=last_month - timedelta(days=30))
    elif date_filter == 'this-year':
        products = products.filter(date__date__year=today.year)
    elif date_filter == 'last-year':
        products = products.filter(date__date__lt=date(today.year, 1, 1), date__date__gte=date(today.year - 1, 1, 1))
    else:
        date_filter = 'All Time'

    
    company_count = Companie.objects.count()
    requested_count = Product.objects.filter(status='pending').count()
    responded_count = Product.objects.filter(status='responded').count()
    total_requested_count = requested_count + responded_count

    context = {
        'products': products,
        'company_count': company_count,
        'total_requested_count': total_requested_count,
        'responded_count': responded_count,
        'query': query,
        'status': status,
        'date_filter': date_filter
        }
    
    return render(request, 'market_research.html', context)


@login_required(login_url='signin')
def detail(request, pk):
    product = Product.objects.get(product_id=pk)
    
    context = {
        'product': product
        }
    return render(request, 'detail_view.html', context)


@login_required(login_url='signin')
def update(request, pk):
    units = Unit.objects.all()
    product = Product.objects.get(product_id=pk)
    company = Companie.objects.get(companiesName=product.company_name)
    
    if request.method == 'POST':
        category = request.POST.get('category')
        product_name = request.POST['product_name']
        quantity = request.POST['quantity']
        description = request.POST['description']
        unit_pk = request.POST.get('unit')
        quantity = request.POST['quantity']
        remark = request.POST['remark']
        unit = Unit.objects.get(pk=unit_pk)
    
        company.category = category
        product.product_name = product_name
        product.quantity = quantity
        product.description = description
        product.unit = unit
        product.remark = remark

        product.save()
        return redirect('update', pk=product.product_id)

    context = {
        'product': product,
        'company': company,
        'units': units
        }
    return render(request, 'update_view.html', context)


@login_required(login_url='signin')
def delete_product(request, pk):
    product = Product.objects.get(product_id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('research')
    return render(request, 'delete_confirmation.html', {'product': product})


def main(request):
    return render(request, 'main.html')


def table(request):
    products = Product.objects.order_by('-date')
    context = {
        'products': products,
        }
    return render(request, 'table.html', context)

def setup(request):
    return render(request, 'setup.html')


def add_setup(request):
    return render(request, 'add_setup.html')

def send_request(request):
    return render(request, 'send_request.html')

