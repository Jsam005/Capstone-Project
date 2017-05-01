from django.conf.urls import include, url
from recipe import views
from account import views as v
app_name = 'account'

urlpatterns = [
    # /recipe/
    url(r'^$', views.home, name='home'),
    url(r'^account/login/$', v.login_view, name='login'),
    url(r'^account/logout/$', v.logout, name='logout'),
    url(r'^account/profile/$', v.profile, name='profile'),
    url(r'^account/register/$', v.register_view, name='register'),
    url(r'^recipe/', include('recipe.urls')),
]