from django.urls import path
from .views import *

urlpatterns = [
    path('home/', TodoList.as_view(), name='home'),
    path('', LoginFormView.as_view(), name='login'),
    path('registration/', MyRegisterFormView.as_view(), name="registration"),
    path('new/', TodoCreate.as_view(), name='create_todo'),
    path('complete/<todo_id>/', completeTodo, name='complete'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='todo_delete'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='todo_update'),
]