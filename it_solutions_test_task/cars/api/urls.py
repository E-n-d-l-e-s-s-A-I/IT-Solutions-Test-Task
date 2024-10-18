from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'cars'

router = SimpleRouter()
router.register(r'cars', views.CarViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('cars/<int:pk>/comments/', views.CommentViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
        }
    )),

    path(r'auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
