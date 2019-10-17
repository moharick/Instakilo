from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    url(r'^register', views.register, name='register'),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'^$', views.home, name='home'),
    url(r'^myaccount/$', views.myprofile, name='myaccount'),
    url(r'^myaccount/edit/$', views.update, name='update'),
    url(r'^comment/(?P<post_id>\d+)$', views.comment_on, name='comment'),
    url(r'^user/(?P<user_id>\d+)$', views.user, name='aboutuser'),
    url(r'^like/(?P<post_id>\d+)$', views.like, name='like'),
    url(r'^save/(?P<post_id>\d+)$', views.save, name='save'),
    url(r'^search/(?P<name>.+)$', views.find, name='save'),
    url(r'^follow_or_not/(?P<user_id>\d+)$', views.togglefollow, name='follow_or_not'),
    url(r'^unlike/(?P<post_id>\d+)$', views.unlike, name='unlike')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)