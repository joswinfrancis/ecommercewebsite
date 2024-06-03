from django.shortcuts import render , get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products':products
    }
    return render(request,'index.html',context)

@login_required(login_url='login')
def products(request,category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)
        paginator = Paginator(products,1)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)


    context = {
        'products':products,
        
    }
    return render(request,'product.html',context)

def search_product(request):
    keyword = request.GET.get('search')

    products = []
    if keyword:
        products = Product.objects.filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))

    context = {
        'products': products
    }
    return render(request, 'product.html', context)

@login_required(login_url='login')
def product_details(request, category_slug, product_slug):
    single_product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    context = {
        'single_product': single_product,
    }
    return render(request, 'product_details.html', context)

def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def blog_list(request):
    return render(request,'blog_list.html')


def testimonials(request):
    return render(request,'testimonial.html')