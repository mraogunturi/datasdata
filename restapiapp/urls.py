from django.urls import path, re_path
from . import views
from django.conf.urls import url, include
from .views import Developers, Users, Apijson, UserInput, UsersApis, UsersOutput, \
    UserOutput, UserUpdate, UserDelete

app_name="restapisapp"

urlpatterns = [

    # path('users/',Users.as_view(), name='users'),
    path('users/',Users.as_view(), name='users'),
    path('developers/', Developers.as_view(), name='developers'),
    path('api/', Apijson),
    path('userget/<str:pk>', UserOutput, name='singleuser'),
    path('usersget/', UsersOutput, name='allusers'),
    path('userpost/', UserInput, name='allusers'),
    path('userupdate/<str:pk>/', UserUpdate, name='userupdate'),
    path('userdelete/<str:pk>/', UserDelete, name='userdelete'),
    path('usersapis/', UsersApis, name='usersapis'),
]