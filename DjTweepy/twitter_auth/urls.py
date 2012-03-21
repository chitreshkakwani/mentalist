
from django.conf.urls.defaults import *
from twitter_auth.views import *

urlpatterns = patterns('twitter_auth.views',
    url(r'^$', view=main, name='main'),
    url(r'^callback/$', view=callback, name='auth_return'),
    url(r'^logout/$', view=unauth, name='oauth_unauth'),
    url(r'^auth/$', view=auth, name='oauth_auth'),
    url(r'^info/$', view=info, name='info'),
<<<<<<< HEAD
    url(r'^save_tweets',view=save_tweets,name='save_tweets'),
=======
    url(r'^savetweets',view=save_tweets,name='save_tweets'),
>>>>>>> 89aa7e23b0b2789d0986b7c01aff694715d5590b
)
