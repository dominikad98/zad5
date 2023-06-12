from django.contrib import admin
from django.urls import path, include
from bazyapp import views
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'kurs', views.KursViewSet)
router.register(r'uczestnik', views.UczestnikViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kurs/<int:kurs_id>/', views.kurs_detail, name='kurs_detail'),
    path('api/token/', ObtainAuthToken.as_view(), name='api_token_auth'),
    path('api/', include(router.urls)),
    
]
