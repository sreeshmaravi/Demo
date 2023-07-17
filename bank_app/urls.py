from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.home,name="home"),
    path('login/', views.login,name="login"),
    path('register/', views.register,name="register"),
    path('member/add/', views.create_view, name='add'),
    path('member/<int:pk>/', views.update_view, name='change'),
 
    path('members/ajax/load-branches/', views.load_branches, name='ajax_load_branches'), # AJAX
    path('newform/', views.newform,name="newform"),
    path('logout',views.logout,name='logout')

]
