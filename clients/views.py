from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blogs.models import Blog
from clients.forms import NewsletterForm, ClientForm, NewsletterManagerForm
from clients.models import Newsletter, Client, Message, MailingAttempt


class NewsletterListView(ListView):
    model = Newsletter
    template_name = "client/newsletter_list.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['blog_list'] = Blog.objects.order_by('?')[:3]
        context['mailing_all'] = len(Newsletter.objects.all())
        context['mailing_active'] = len(Newsletter.objects.filter(status='started'))
        context['client_unique'] = len(Client.objects.all().distinct())
        return context


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy("client:letter_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy("client:letter_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return NewsletterForm
        elif user.has_perm("client:can_view_any_mailings") and user.has_perm('can_disable_mailings') and user.has_perm('can_view_the_list_of_service_users') and user.has_perm('can_block_users_of_the_service'):
            return NewsletterManagerForm
        raise PermissionDenied


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy("client:letter_list")

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.owner == self.request.user:
            return obj
        raise PermissionDenied


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter
    template_name = "client/letter_detail.html"


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client/client_list.html'


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client/client_detail.html'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client:client_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'client/message_list.html'


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'client/message_detail.html'


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('client:message_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('client:message_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.owner == self.request.user:
            return obj
        raise PermissionDenied


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('client:message_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.owner == self.request.user:
            return obj
        raise PermissionDenied


class MailingAttemptListView(LoginRequiredMixin, ListView):
    model = MailingAttempt
    template_name = 'client/mailingattempt_list.html'