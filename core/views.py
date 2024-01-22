from django.shortcuts import redirect, render

from django.http import HttpResponse
from core.forms import ContactForm

from core.models import *

# Create your views here.


def home(request):
    context = {
        "title": "Home page",
        "products": Products.objects.all(),
        "testimonials": Testimonial.objects.all(),
    }
    return render(request, "index.html", context)


def about(request):
    context = {
        "title": "About",
        "testimonials": Testimonial.objects.all(),
        "video": About.objects.first(),  # Assuming there's only one video in About
    }
    return render(request, "about.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")
    else:
        form = ContactForm()

    context = {
        "title": "Contact Page",
        "form": form,
    }
    return render(request, "contact.html", context=context)


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Products  # Products modelini gerektiği gibi güncelleyin


def products(request):
    clothing = Clothing.objects.all()
    jeans = Jeans.objects.all()
    all_products = Products.objects.all()

    if "clothing" in request.GET:
        # Kullanıcının seçtiği kıyafet türüne göre ürünleri filtrele
        all_products = all_products.filter(clothing_id__title=request.GET["clothing"])
    if "jeans" in request.GET:
        # Kullanıcının seçtiği kıyafet türüne göre ürünleri filtrele
        all_products = all_products.filter(jeans_id__title=request.GET["jeans"])

    items_per_page = 3
    paginator = Paginator(all_products, items_per_page)
    page = request.GET.get("page")

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        "title": "Products Page",
        "products": products,
        "clothing": clothing,
        "jeans": jeans,
    }

    return render(request, "shop.html", context)


def news(request):
    tag=Tag.objects.all()
    input_ = request.GET.get("news")
    

    if input_:
        all_news = News.objects.filter(title__icontains=input_)
    else:
        all_news = News.objects.all()
        
    if "tag" in request.GET:
        all_news = all_news.filter(tag_id__title=request.GET["tag"])
        
    context = {
        "title": "Blog Page",
        "all_news": all_news,
        "news_count": all_news.count(),
        "empty": "No News Found",
        "tag":tag
    }
    return render(request, "blog.html", context=context)


def product_single(request, id):
    context = {
        "title": "Product Single Page",
        "product_single": Products.objects.get(id=id),
        "products": Products.objects.all().order_by("created_at"),
    }
    return render(request, "product-single.html", context=context)


def news_single(request, id):
    all_news=News.objects.all()
    context = {
        "title": "News Single Page",
        "news_single": News.objects.get(id=id),
        "all_news": all_news,
        "news": News.objects.all().order_by("created_at"),
    }
    return render(request, "blog-single.html", context=context)


def search(request):
    input_ = request.GET.get("search")
    if input_:
        if Products.objects.filter(title__icontains=input_).exists():
            return redirect("products")
        elif News.objects.filter(title__icontains=input_).exists():
            return redirect("news")

    return render(request, "index.html")
