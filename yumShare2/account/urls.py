from django.conf.urls import include, url
from recipe import views
from account import views as v
app_name = 'account'

urlpatterns = [
    # /recipe/
    url(r'^$', views.home, name='home'),
    url(r'^login/$', v.login_view, name='login'),
    url(r'^logout/$', v.logout_view, name='logout'),
    url(r'^register/$', v.register_view, name='register'),
    url(r'^profile/', v.profile_view, name='profile'),
    url(r'^profile/edit/$', v.edit_profile_view, name='edit-profile'),
    url(r'^change-password/$', v.change_password_view, name='change-password'),
    #url(r'^profile/(?P<username>[\w.@+-]+)/$', v.profile_view, name='profile'),
    url(r'^recipe/', include('recipe.urls')),
]