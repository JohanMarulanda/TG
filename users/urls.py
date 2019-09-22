from django.conf.urls import url
from users import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'users'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^register/$',views.register,name='register'),
    path('user_logout',views.user_logout,name='user_logout'),
    url(r'^principalUser/$',views.principalUser,name='principalUser'),
]
