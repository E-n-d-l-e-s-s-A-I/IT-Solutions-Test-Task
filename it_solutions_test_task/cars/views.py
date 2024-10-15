from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView
from django.views.generic.edit import FormMixin


from .forms import CommentForm
from .models import Car
from .mixins import CarListMixin, CarEditMixin


class Homepage(CarListMixin):
    template_name = 'cars/index.html'


class CarDetailView(FormMixin, DetailView):
    model = Car
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('cars:car_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("У вас нет прав добавлять объект.")
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.car = self.object
        comment.save()
        return super().form_valid(form)

    def get_queryset(self):
        return Car.objects.filter(
            pk=self.kwargs['pk']
            ).select_related('owner').prefetch_related('comments__author')


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ('make', 'model', 'year', 'description')
    success_url = reverse_lazy('cars:homepage')

    def form_valid(self, form):
        car = form.save(commit=False)
        car.owner = self.request.user
        car.save()
        return super().form_valid(form)


class MyCarListView(LoginRequiredMixin, CarListMixin):
    template_name = 'cars/my_car_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class CarDeleteView(CarEditMixin, DeleteView):
    template_name = 'cars/car_confirm_delete.html'
    success_url = reverse_lazy('cars:my_cars')


class CarUpdateView(CarEditMixin, UpdateView):
    fields = ('make', 'model', 'year', 'description')
