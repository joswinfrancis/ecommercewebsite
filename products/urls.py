from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index , name="index"),
    path('products/',views.products , name='products'),
    path('products/<slug:category_slug>/',views.products , name='products_by_category'),
    path('products/<slug:category_slug>/<slug:product_slug>/',views.product_details , name='product_details'),
    path('search_product/',views.search_product , name='search_product'),
    path('about/',views.about , name='about'),
    path('contact/',views.contact , name='contact'),
    path('blog_list/',views.blog_list , name='blog_list'),
    path('testimonials/',views.testimonials , name='testimonials'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)