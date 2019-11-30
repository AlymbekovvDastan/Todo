from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.shortcuts import render, redirect

class Todo(models.Model):
	text = models.TextField()
	status = models.BooleanField(default=False)
	user_todo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

	def get_absolute_url(self):
		return reverse('todo_update',kwargs={'pk':self.pk})

	def __str__(self):
		return self.text