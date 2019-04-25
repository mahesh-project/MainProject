"""sportss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app1 import views
from django.conf  import settings
from django.conf.urls.static import static

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('index/', views.index),
    path('reg/', views.reg),
    path('add_cat/', views.add_cat),
    path('busisave/', views.busisave),
    path('catsave/', views.catsave),
    path('add_court/', views.add_court),
    path('courtsave/', views.courtsave),
    path('view_Category/', views.cat1),
    path('view_court/', views.cat2),
    path('add_tour/', views.add_tour),
    path('toursave/', views.toursave),
    path('add_team/', views.add_team),
    path('teamsave/', views.teamsave),
    path('add_member/', views.add_member),
    path('membersave/', views.membersave),
    path('log/', views.log),
    path('admin/', views.admin1),
    path('customer/', views.customer1),
    path('bussiness/', views.bussiness1),
    path('verify_buss/', views.verify_buss),
    path('verify/<int:id>', views.verify),
    path('verifysave/<int:id>', views.verifysave),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)