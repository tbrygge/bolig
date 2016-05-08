"""bo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.forms import AdminPasswordChangeForm
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
     url(r'^accounts/password_change/$',  # hijack password_change's url
        'django.contrib.auth.views.password_change',        
        name="password_change"),
     url(r'^accounts/password_change/done/$',  # hijack password_change's url
        'django.contrib.auth.views.password_change_done',        
       name="password_change_done"),    
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'', include('bolig.urls')),
]
admin.site.site_header = 'Tananger brygge - administrasjon'