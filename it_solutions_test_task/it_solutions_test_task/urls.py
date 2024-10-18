from django.conf import settings
from django.contrib import admin
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("cars.urls", namespace="cars")),
    path('login/', auth.views.LoginView.as_view(), name='login'),
    path('logout/', auth.views.LogoutView.as_view(), name='logout'),
    path(
        'registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('cars:homepage'),
        ),
        name='registration',
    ),
    path('api/', include('cars.api.urls', namespace='api')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
