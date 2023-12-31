from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('finished/', views.finished_tasks, name='finished_tasks'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.list_element, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('finish_record/<int:pk>', views.mark_as_finished, name='finish_record'),
    path('restore_record/<int:pk>', views.mark_as_unfinished, name='restore_record'),
    path('finished_record/<int:pk>', views.finished_element, name='finished_record'),
    path('update_finished_record/<int:pk>', views.update_finished_record, name='update_finished_record'),
]