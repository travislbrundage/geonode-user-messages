from django.conf.urls import url

from . import views

app_name = "messages"


urlpatterns = [  # "user_messages.views",
    url(r"^inbox/$", views.inbox, name="inbox"),
    url(r"^create/$", views.message_create, name="create"),
    url(r"^create/(?P<user_id>\d+)/$", views.message_create, name="create"),
    url(r"^create/_multiple/$", views.message_create, name="create_multiple"),
    url(r"^thread/(?P<thread_id>\d+)/$", views.thread_detail,
        name="thread_detail"),
    url(r"^thread/(?P<thread_id>\d+)/delete/$", views.thread_delete,
        name="thread_delete"),
]
