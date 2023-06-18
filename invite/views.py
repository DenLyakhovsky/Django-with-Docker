from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import FormView, DetailView, ListView, TemplateView
from .models import *
from .forms import *


class MainPage(ListView):
    model = Goods
    template_name = 'invite/main_page.html'
    context_object_name = 'main_view'


class DetailGoods(DetailView):
    model = Goods
    template_name = 'invite/detail_goods.html'
    context_object_name = 'detail_goods_view'


class ViewForm(FormView):
    form_class = PersonForm
    template_name = 'invite/form.html'

    # Зберігає користувача в БД
    def form_valid(self, form):
        cd = form.cleaned_data
        person = Person(name=cd.get('name'), last_name=cd.get('last_name'))
        person.save()
        return redirect('successful_form_page')


class SuccessfulForm(TemplateView):
    template_name = 'invite/successful.html'


class InfoAboutUser(DetailView):
    model = Person
    template_name = 'invite/info_user.html'
    context_object_name = 'info_user_view'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Отримуємо pk
        user_id = self.kwargs['pk']

        # Встановлення cookie
        response = HttpResponse("User info is set!")
        response.set_cookie('user_id', user_id)

        # Додаємо pk до контексту шаблону
        context['user_id'] = user_id

        return context


def room(request, room_name):
    return render(request, "invite/room.html", {"room_name": room_name})
