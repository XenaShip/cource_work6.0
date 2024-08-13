from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views import generic

from .form import MailForm, LetterForm, ClientForm
from .models import Client, Mail, Letter


class MailsListView(generic.ListView):
    model = Mail
    template_name = 'main/mails_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Список рассылок'
        return context_data

    def get_queryset(self):
        return Mail.objects.filter(user=self.request.user)


class MailUpdateView(generic.UpdateView):
    model = Mail
    form_class = MailForm
    extra_context = {
        'title': 'Изменение рассылки'
    }
    success_url = reverse_lazy('main:mails_list')


class MailDeleteView(generic.DeleteView):
    model = Mail
    success_url = reverse_lazy('main:mails_list')


class MailCreateView(generic.CreateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('main:mails_list')
    extra_context = {
        'title': 'Создание рассылки'
    }

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LetterCreateView(generic.CreateView):
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy('main:letters_list')
    extra_context = {
        'title': 'Создание письма'
    }


class LetterDeleteView(generic.DeleteView):
    model = Letter
    success_url = reverse_lazy('main:letters_list')


class LetterUpdateView(generic.UpdateView):
    model = Letter
    form_class = LetterForm
    extra_context = {
        'title': 'Изменение письма'
    }
    success_url = reverse_lazy('main:letters_list')


class ClientUpdateView(generic.UpdateView):
    model = Client
    form_class = ClientForm
    extra_context = {
        'title': 'Изменение клиента'
    }
    success_url = reverse_lazy('main:clients_list')


class ClientDeleteView(generic.DeleteView):
    model = Client
    success_url = reverse_lazy('main:clients_list')


class ClientCreateView(generic.CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:clients_list')
    extra_context = {
        'title': 'Создание клиента'
    }


class ClientsListView(generic.ListView):
    model = Client
    template_name = 'main/clients_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Список клиентов'
        return context_data

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)


class MailDetailView(generic.DetailView):
    model = Mail
    template_name = 'main/mail_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data


class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'main/client_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data


class LetterDetailView(generic.DetailView):
    model = Letter
    template_name = 'main/letter_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data


class LetterListView(generic.ListView):
    model = Letter
    template_name = 'main/letters_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Список писем'
        return context_data

    def get_queryset(self):
        return Letter.objects.filter(user=self.request.user)
