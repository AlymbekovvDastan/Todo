from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, TemplateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy
from .forms import TodoForm

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
    

class TodoList(FormView,ListView):
    model = Todo
    template_name = 'todo_app/home.html'
    form_class = TodoForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user_todo = self.request.user
        print(form.instance.user_todo)
        a = self.request.POST.get('text', False)
        Todo.objects.create(text=a, user_todo=form.instance.user_todo)
        # print(self.request.status)
        return super().form_valid(form)

    def get_queryset(self):
        return Todo.objects.filter(user_todo=self.request.user)


class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('home')


class TodoUpdate(UpdateView):
    model = Todo
    success_url = reverse_lazy('home')
    template_name = 'todo_app/todo_update.html'
    fields = ['text',]
   

    
def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.status = True
    todo.save()

    return redirect('home')