from django.conf.urls import include, url
from recipe import views
from account import views as v
app_name = 'account'

urlpatterns = [
    # /recipe/
    url(r'^$', views.home, name='home'),
    url(r'^login/$', v.login_view, name='login'),
    url(r'^logout/$', v.logout_view, name='logout'),
    url(r'^profile/$', v.profile, name='profile'),
    url(r'^register/$', v.register_view, name='register'),
    url(r'^recipe/', include('recipe.urls')),
]