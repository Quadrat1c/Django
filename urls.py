from django.urls import path

# Implementation of views in path
from .views import views
from appName import views

urlpatterns = [
  path('<filename>.html', views.html),
  path('', views.index),
]


# Bootstrap - Static theme folder
from bootstrap import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls), #from django.contrib import admin
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Static implementation
'''
return [
        re_path(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), view, kwargs=kwargs),
]
'''
