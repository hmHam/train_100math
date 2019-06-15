"""train_100math URL Configuration

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
from train_100math.app.views import Train100MathView, NBackView, hello_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('train_100math/', Train100MathView.as_view(), name='train_100math'),
    path('n_back/', NBackView.as_view(), name='n_back'),
    path('', hello_template)
]
