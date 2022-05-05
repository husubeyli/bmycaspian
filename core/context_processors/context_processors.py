from core.models import AboutPageContent, Navbar, WebsiteSettings, Service, StaticText

def base_html_context(request):
    print([obj.order for obj in StaticText.objects.all().order_by("order")], 'necesen')
    context = {
        "navbar": Navbar.objects.filter(is_active = True).order_by("order"),
        "settings": WebsiteSettings.objects.all().last(),
        "services": Service.objects.filter(is_active = True).order_by("order"),
        "static": StaticText.objects.all().order_by("order"),
        "about_contents": AboutPageContent.objects.all().last(),

    }
    return context