from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, TemplateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy

''' Регистрация '''
class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/registration.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "registration/login.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
    

class TodoList(ListView):
    model = Todo
    template_name = 'todo_app/home.html'
    
    def get_queryset(self):
        return Todo.objects.filter(user_todo=self.request.user)


class TodoCreate(CreateView):
    model = Todo
    template_name = 'todo_app/create_todo.html'
    fields = ['text', ]
    context_object_name = 'create_todo'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user_todo = self.request.user
        return super(TodoCreate, self).form_valid(form)


class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('home')


class TodoUpdate(UpdateView):
    model = Todo
    template_name = 'todo_app/todo_update.html'
    fields = ['text', 'user_todo']
    success_urls = reverse_lazy('home')

    
def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.status = True
    todo.save()

    return redirect('home')