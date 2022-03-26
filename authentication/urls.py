from django.contrib import admin
from django.urls import path, include
from authentication import views
from .views import chartData
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='authentication'),
    path('register', views.register, name='registration'),
    path('login', views.index, name='authentication'),
    path('signin', views.signin, name='signin'),
    path('logout',views.logout_request,name='logout_request'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('api/chart/data',  chartData.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()