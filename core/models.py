from typing import Text
from xmlrpc.client import boolean
from django.db import models
from django.conf import settings
from django.forms import CharField
from django.utils.text import slugify
from ckeditor.fields import RichTextField

from core.tools import get_about_page_signature


class Navbar(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)
    order = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class WebsiteSettings(models.Model):
    company_name = models.CharField(max_length=255, blank=True, null=True)
    orange_logo = models.ImageField(upload_to="logo/")
    white_logo = models.ImageField(upload_to="logo/")
    footer_text = models.CharField(max_length=500, blank=True, null=True)
    footer_logo = models.ImageField(upload_to="logo/", blank=True, null=True)
    promotion_video_url = models.URLField(blank=True, null=True)
    promotion_video_image = models.ImageField(upload_to="logo/")
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    address_link = models.CharField(max_length=255)
    instagram_address = models.URLField()
    facebook_address = models.URLField()
    whatsapp_address = models.URLField()
    about_us_page = models.BooleanField(default=False)
    years_experience = models.IntegerField(default=0)
    
    
    def __str__(self):
        return 'Site settings'
    
    

class AboutPageContent(models.Model):
    signature = models.ImageField(upload_to=get_about_page_signature, blank=True, null=True)
    author_fullname = models.CharField(max_length=255, blank=True, null=True)
    author_position = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"
        
    def __str__(self):
        return "About Page Content"


class Service(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(unique=True)
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    icon = models.ImageField(upload_to="services/", blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProjectStatistics(models.Model):
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}/ {self.number}'


class Projects(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="projects/")
    tags = models.ManyToManyField("ProjectCategories", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectCategories(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(unique=True, default=0)

    def __str__(self):
        return self.title


class Products(models.Model):
    project_id = models.ManyToManyField("Projects", blank=True)
    name = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products/")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'project by {self.project_id}/{self.name}'


class Clients(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)
    order = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="clients/")
    image_2 = models.ImageField(upload_to="clients/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return ''
        
    def get_image_2_url(self):
        if self.image_2 and hasattr(self.image_2, 'url'):
            return self.image_2.url
        else:
            return ''

    
    
class Partners(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)
    order = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="partners/")
    image_2 = models.ImageField(upload_to="partners/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="team_members/", blank=True, null=True)
    socials = models.ManyToManyField("SocialAccount", related_name="socials", blank=True,
                                     limit_choices_to={"is_company": False})

    def __str__(self):
        return self.name + ' ' + self.surname

    @property
    def full_name(self):
        return self.name + ' ' + self.surname


class SocialAccount(models.Model):
    icon = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField()
    name = models.CharField(max_length=255, blank=True, default="")
    teammember_name = models.CharField(max_length=255, blank=True, null=True)
    is_company = models.BooleanField()

    def __str__(self):
        return f"{self.name} - {self.teammember_name}"


class News(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="news")
    description = RichTextField(blank=True, null=True)
    category = models.ForeignKey(ProjectCategories, on_delete=models.PROTECT, related_name="news")
    image = models.ImageField(upload_to="news/")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name + self.subject


class Addesses(models.Model):
    image = models.ImageField(upload_to='addresses/')
    type_name = models.CharField(max_length=100)
    full_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100, default='+994')
    email = models.EmailField()


# ////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////INDEX PAGE STATIC Text/////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////

class StaticText(models.Model):
    text_placement = models.CharField(max_length=255, help_text="Example: index page - banner")
    surtitle = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    bullet_points = models.JSONField(default=list, blank=True)
    order = models.PositiveSmallIntegerField()
    image_1 = models.ImageField(upload_to="static/", blank=True, null=True)
    image_2 = models.ImageField(upload_to="static/", blank=True, null=True)

    def __str__(self):
        return f"{self.text_placement}"

    def get_image_1_url(self):
        if self.image_1 and hasattr(self.image_1, 'url'):
            return self.image_1.url
        else:
            return ''

    def get_image_2_url(self):
        if self.image_2 and hasattr(self.image_2, 'url'):
            return self.image_2.url
        else:
            return ''
        
        
class BulletPoint(models.Model):
    # relations
    static_text = models.ForeignKey(StaticText, on_delete=models.CASCADE, related_name="bullets_points", blank=True, null=True)
    
    # moderations
    title = models.CharField(max_length=1000)
    
    def __str__(self):
        return f"{self.title}"