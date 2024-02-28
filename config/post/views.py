from django.shortcuts import render
from django.views import generic
from . models import post_model
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy

# Create your views here.
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = post_model
    template_name = 'post/post_update.html'
    fields = ['title','description']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post  = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    success_url ='/'
class post_delete(LoginRequiredMixin,UserPassesTestMixin, generic.DeleteView):
    model = post_model
    template_name = 'post/delete.html'
    def test_func(self):
        post  = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    success_url ='/'

class PostCreate(LoginRequiredMixin,generic.CreateView):
    model = post_model
    template_name = 'post/postCreate.html'
    fields = ['title','description']
    success_url = '/'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDetails(generic.DetailView):
    model = post_model
    template_name = 'post/details.html'



class homeView(generic.ListView):
    model = post_model
    template_name = 'post/index.html'
    context_object_name = 'post_data'
    ordering = ['-id']
# def homeView(request):
#     posts = post_model.objects.all()
#     return render(request, 'post/index.html', {'posts': posts})