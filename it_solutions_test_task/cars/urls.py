from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.Homepage.as_view(), name='index'),
    path('cars/', views.Homepage.as_view(), name='homepage'),
    path('my_cars/', views.MyCarListView.as_view(), name='my_cars'),

    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),

    path('cars/add/', views.CarCreateView.as_view(), name='car_add'),
    path(
        'cars/delete/<int:pk>/',
        views.CarDeleteView.as_view(),
        name='car_delete'
    ),
    path(
        'cars/edit/<int:pk>/',
        views.CarUpdateView.as_view(),
        name='car_edit'
    ),
]
