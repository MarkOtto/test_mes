from django.conf.urls import url, include
#from rest_framework import routers
from . import views
from rest_framework.authtoken import views as drf


#router = routers.DefaultRouter()
#router.register('msg', views.MessageViewSet)


urlpatterns = [
    url(r'^token/$', drf.obtain_auth_token),
    url(r'^register/$', views.RegisterView.as_view()),
    url(r'^users/$', views.UsersView.as_view(), name='messages_all'),
    url(r'^send/$',  views.SendView.as_view(), name='send_new'),
    url(r'^sent/$',  views.SentView.as_view(), name='messages_sent'),
    url(r'^inbox/$', views.InboxView.as_view(), name='messages_inbox'),
    url(r'^messages/$', views.MessagesView.as_view(), name='messages_all'),
    url(r'^message/(?P<pk>\d+)/$', views.MessageDetailView.as_view(), name='message_details'),
    #url(r'^', include(router.urls)),
]