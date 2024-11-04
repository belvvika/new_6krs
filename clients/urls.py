from django.urls import path
from django.views.decorators.cache import cache_page

from clients.apps import ClientsConfig
from clients.views import NewsletterListView, NewsletterCreateView, NewsletterDetailView, \
    NewsletterDeleteView, NewsletterUpdateView, ClientListView, ClientCreateView, ClientDetailView, \
    ClientUpdateView, ClientDeleteView, MessageListView, MessageCreateView, MessageDetailView, MessageUpdateView, \
    MessageDeleteView, MailingAttemptListView

app_name = ClientsConfig.name

urlpatterns = [

    path('', cache_page(60)(NewsletterListView.as_view()), name='newsletter_list'),
    path('create/', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('detail/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('update/<int:pk>/', NewsletterUpdateView.as_view(), name='newsletter_form'),
    path('delete/<int:pk>/', NewsletterDeleteView.as_view(), name='newsletter_confirm_delete'),

    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_form'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_confirm_delete'),

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_form'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_confirm_delete'),

    path('log_list/', MailingAttemptListView.as_view(), name='mailingattempt_list')

]