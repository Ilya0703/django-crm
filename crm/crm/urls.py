"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crmDjango import views

urlpatterns = [
    path("", views.index),
    path("applications", views.applicationsView, name="applications"),
    path("clients", views.clientsView, name="clients"),
    path("products", views.productsView, name="products"),
    path("sales", views.salesView, name="sales"),
    path("workers", views.workersView, name="workers"),
    path("applications_report", views.applicationsReportsView, name="applications_report"),
    path("sales_report", views.salesReportsView, name="sales_report"),
    path("clients_report", views.clientsReportsView, name="clients_report"),
    path("products_report", views.productsReportView, name="products_report"),
    path("create_application", views.createApplication, name="create_application"),
    path("create_product", views.createProduct, name="create_product"),
    path("create_worker", views.createWorker, name="create_worker"),
]
