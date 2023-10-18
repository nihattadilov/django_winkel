from django.shortcuts import redirect, render

from django.http import HttpResponse
from core.forms import ContactForm

from core.models import Setting, Products, Testimonial, News

# Create your views here.


def home(request):
    context = {
        "title": "Home page",
        "products": Products.objects.all(),
        "testimonials": Testimonial.objects.all(),
    }
    return render(request, "index.html", context)


def about(request):
    context = {"title": "About", "testimonials": Testimonial.objects.all()}
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


def products(request):
    products = Products.objects.all()

    for product in products:
        if product.discount > 0:
            product.discounted_price = product.price - (
                product.price * product.discount / 100
            )
        else:
            product.discounted_price = product.price

    input_ = request.GET.get("products")

    if input_:
        all_products = Products.objects.filter(title__icontains=input_)
    else:
        all_products = Products.objects.all()

    context = {
        "title": "Products Page",
        "products": all_products,
    }
    return render(request, "shop.html", context=context)


def news(request):
    input_ = request.GET.get("news")

    if input_:
        all_news = News.objects.filter(title__icontains=input_)
    else:
        all_news = News.objects.all()

    context = {
        "title": "Blog Page",
        "all_news": all_news,
        "news_count": all_news.count(),
        "empty": "No News Found",
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
    context = {
        "title": "News Single Page",
        "news_single": News.objects.get(id=id),
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
