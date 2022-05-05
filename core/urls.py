from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView, name="index"),
    path('about/', views.AboutView, name="about"),
    path('services/', views.ServicesView, name="services"),
    path('services/<int:id>', views.ServicesDetailView, name="services-detail"),
    path('projects/', views.ProjectsView, name="projects"),
    path('project-detail/<slug:slug>', views.ProjectDetailView, name="project-detail"),
    path('products/', views.ProductsView, name="products"),
    path('product-detail/<slug:slug>', views.ProductDetailView, name="product-detail"),
    path('partners/', views.PartnersView, name="partners"),
    path('clients/', views.ClientsView, name="clients"),
    path('news/', views.NewsView, name="news"),
    path('news/<slug:slug>', views.NewsDetailView, name="news-detail"),
    path('contact/', views.ContactView, name="contact"),
    path('search/', views.SearchResultView, name="search_result"),


]