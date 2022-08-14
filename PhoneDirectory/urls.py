"""PhoneDirectory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from contacts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Phone-Directory-App/', views.Home.as_view(), name='home'),
    path('create', views.CreateContact.as_view(), name='create_contact'),
    path('update<int:pk>', views.UpdateContact.as_view(), name='update_contact'),
    path('delete<int:pk>', views.DeleteContact.as_view(), name='delete_contact'),
    path('detail<int:pk>', views.ContactDetail.as_view(), name='contact_detail'),
    path('addcontact', views.addcontact, name='add_contact'),
    path('updatepage/', views.updatepage),
    path('updateexistcont', views.updateexistcont),
    path('delpage/', views.delpage),
    path('delcontact', views.delcontact),
    path('searchpage/', views.searchpage),
    path('searchbyname/', views.searchbyname),
]
