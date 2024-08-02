from django.urls import path
from . import views

urlpatterns = [
    # path('chat/send_message/', views.send_messages, name='send_message'),
    path('get_chat_history/', views.get_chat_history, name='get_chat_history'),
    path('chat_page/', views.chat_page, name='chat_page'),
]