"""SitioWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from GestionLab import views

urlpatterns = [

    path('login/', views.login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('register/', views.register_user, name="register"),
    # url(r'^login/$',
    #     views.LoginView.as_view(success_url='/'),
    #     name='login',
    #     kwargs={'authentication_form': LoginForm}),
    # url(r'^logout/$',
    #     views.LogoutView.as_view(),
    #     name='logout'),

    path('admin/', admin.site.urls, name='admin'),
    path('tinymce/', include('tinymce.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', views.homepage, name='home'),
    path('login/', views.materiales, name='login'),
    path('materiales/', views.materiales, name='materiales'),
    path('convocatorias/', include('Convocatorias.urls', namespace='convocatorias')),
    path('reservaciones/', include('Reservacion.urls', namespace='reservaciones')),

]
urlpatterns += staticfiles_urlpatterns()
