from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Partners, ProjectCategories, Projects, Clients, Service, TeamMember, News, Products,ProjectStatistics,WebsiteSettings,Addesses
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import JsonResponse


def IndexView(request):
    context = {}
    context["projects"] = Projects.objects.filter(is_active=True).order_by("-created_at")[:6]
    context["clients"] = Clients.objects.filter(is_active=True).order_by("-created_at")[:8]
    return render(request, 'index.html', context)


def AboutView(request):
    context = {}
    context["teammembers"] = TeamMember.objects.all()

    return render(request, 'about-us.html', context)


def ServicesView(request):
    context = {}
    return render(request, 'our-services.html', context)


def ServicesDetailView(request, id):
    service = Service.objects.filter(id=id).first()

    return render(request, "inside-services.html", {"service": service})


def ProjectsView(request):
    context = {}
    # count = 4

    # if request.is_ajax():
    #     upper = int(request.GET.get("vis", None))
    #     if upper:
    #         lower = upper - 3
    #         projects = list(Projects.objects.values())[lower:upper]
    #         return JsonResponse({"data": projects}, safe = False)

    context["categories"] = ProjectCategories.objects.all()
    context['project_statistics'] = ProjectStatistics.objects.all()
    if request.GET.get("category", None):
        context["projects"] = Projects.objects.filter(is_active=True, tags__title=request.GET["category"]).order_by(
            "-created_at")
        context["filter_category"] = request.GET["category"]
    else:
        context["projects"] = Projects.objects.filter(is_active=True).order_by("-created_at")

    return render(request, "our-projects.html", context)


def ProductsView(request):
    context = {}
    context["products"] = Products.objects.filter(is_active=True).order_by("-created_at")

    return render(request, "our-products.html", context)


def ClientsView(request):
    context = {}
    context["clients"] = Clients.objects.filter(is_active=True).order_by("-created_at")[:8]

    return render(request, "our-client.html", context)

def PartnersView(request):
    context = {
        'partners': Partners.objects.filter(is_active=True).order_by("-created_at")[:8]
    }
    
    return render(request, 'our-partners.html', context)

def NewsView(request):
    news_list = News.objects.all().order_by("-created_at")
    page = request.GET.get("page", 1)
    paginator = Paginator(news_list, 9)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, "three-column-blog.html", {"news": news})


def NewsDetailView(request, slug):
    news = News.objects.filter(slug=slug).first()

    return render(request, "inside.html", {"news": news})


def ProjectDetailView(request, slug):
    project_detail = Projects.objects.filter(slug=slug).first()
    products = Products.objects.filter(is_active=True, project_id=project_detail)
    return render(request, "project_detail.html", {"project_detail": project_detail,
                                                   "products": products})


def ProductDetailView(request, slug):
    product_detail = Products.objects.filter(slug=slug).first()

    return render(request, "product_detail.html", {"product_detail": product_detail})


def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        my_email = settings.DEFAULT_FROM_EMAIL
        if form.is_valid():
            name = form.cleaned_data["name"]
            subject = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            email = EmailMessage(subject, message, my_email, [my_email], reply_to=[email])
            email.send()
            form.save()
            return HttpResponseRedirect(reverse("core:index"))
    else:
        form = ContactForm()
        setting = WebsiteSettings.objects.all().first()
        addresses = Addesses.objects.all()
        return render(request, 'contact-us.html', {'form': form,
                                                   'setting': setting,
                                                   'addresses': addresses})


def SearchResultView(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', False)
        products = Products.objects.filter(name__contains=searched)
        return render(request, 'search-result.html', {'products':products,'searched':searched})

    return render(request, 'search-result.html', {})
