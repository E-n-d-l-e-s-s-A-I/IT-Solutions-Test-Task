from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView

from .models import Car


class CarListMixin(ListView):
    model = Car
    context_object_name = 'cars'


class CarEditMixin(LoginRequiredMixin):
    model = Car
    success_url = reverse_lazy('cars:my_cars')

    def dispatch(self, request, *args, **kwargs):
        car = self.get_object()
        if car.owner != self.request.user:
            raise PermissionDenied("У вас нет прав изменять этот объект.")
        return super().dispatch(request, *args, **kwargs)
