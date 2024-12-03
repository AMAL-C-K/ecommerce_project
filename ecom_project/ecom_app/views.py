from django.shortcuts import render
from django.db.models import Q
from ecom_app.models import Category, Products
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger

# Create your views here.

def home(request):
    category = Category.objects.all()
    offer = Products.objects.filter(offer=True)
    trending_smartphones = Products.objects.filter(trending=True, category__category_name='SMARTPHONES')
    trending_laptops = Products.objects.filter(trending=True, category__category_name='LAPTOPS')
    context = {
        'category': category,
        'offer': offer,
        'trending_smartphones': trending_smartphones,
        'trending_laptops': trending_laptops,
    }
    return render(request, 'index.html', context)


def product_detail(request, c_slug, p_slug):
    try:
        product = Products.objects.get(category__slug=c_slug, slug=p_slug)
    except Exception as e:
        raise e
    context = {
        'product': product,
    }
    return render(request, 'single_product.html', context)


def catergories(request, c_slug):
    catergory_wise_products = Products.objects.filter(category__slug=c_slug)
     
    context = {
        'category': catergory_wise_products,
        'slug':c_slug,
    }
    return render(request, 'category_list.html', context)


def search(request):
    products = None
    q = None
    if 'q' in request.GET:
      query = request.GET.get('q')  
      products = Products.objects.filter(Q(category__category_name__contains=query)|Q(brand__brand_name__contains=query)| Q(name__contains=query)|Q(description__contains=query)| Q(tag__contains=query))
      
    return render(request, 'search.html', {'products':products, 'query':query})