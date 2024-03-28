from django.urls import path,include
from .views import loginpage,Userlogout,register,home,delete_tasks,update_tasks
urlpatterns = [
  path('login/',loginpage,name='loginpath'),
  path('logout/',Userlogout,name='logoutpath'),
  path('register/',register,name='registerpath'),
  path('',home,name='home-page'),
  path('delete/<str:name>',delete_tasks,name='delete'),
  path('update/<str:name>',update_tasks,name='update')
   
]