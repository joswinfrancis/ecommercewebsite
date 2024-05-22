from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def products(request):
    return render(request,'product.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def blog_list(request):
    return render(request,'blog_list.html')


def testimonials(request):
    return render(request,'testimonial.html')