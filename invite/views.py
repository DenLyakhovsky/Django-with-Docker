from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import FormView, DetailView
from .models import *
from .forms import *


class HomeFormView(FormView):
    form_class = PersonForm
    template_name = 'invite/home.html'

    def form_valid(self, form):
        cd = form.cleaned_data
        person = Person(name=cd.get('name'), last_name=cd.get('last_name'))
        person.save()
        return redirect('info_about_user', pk=person.pk)


class InfoAboutUser(DetailView):
    model = Person
    template_name = 'invite/info_user.html'
    context_object_name = 'info_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Отримуємо ID користувача з URL-параметра "pk"
        user_id = self.kwargs['pk']

        # Встановлюємо значення cookie для ID користувача
        response = HttpResponse("User info is set!")
        response.set_cookie('user_id', user_id)

        # Додаємо ID користувача до контексту шаблону
        context['user_id'] = user_id

        return context
