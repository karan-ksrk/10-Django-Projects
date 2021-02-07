from django.shortcuts import render
from django.views import generic
from .models import Posts

class add_post(generic.CreateView):
    model = Posts
    fields = ["post_title", "post_description", "comment", "tags", "user_details"]

class update_post(generic.UpdateView):
    model = Posts
    template_name = 'djangoCRUDAPP/update.html'
    fields = ["post_title", "post_description", "comment", "tags", "user_details"]

class delete_post(generic.DeleteView):
    model = Posts


class read_post(generic.DetailView):
    model = Posts


class read_post_all(generic.ListView):
    model = Posts
    template_name = 'djangoCRUDAPP/index.html'