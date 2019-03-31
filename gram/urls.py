"""gram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from main import views as main_views
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

app_name='gram'

urlpatterns = [ path('',main_views.mainf,name='home'),
    path('admin/', admin.site.urls),
    path('signup/',include('usersignup.urls')),
    path('login/',auth_views.login,{'template_name': 'main/login.html'}, name='login'),
    path('logout/',auth_views.logout, {'next_page': '/'}, name='logout'),
    path('accounts/',include('main.urls')),
   
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)