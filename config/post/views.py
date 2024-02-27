from django.shortcuts import render
from django.views import generic
from . models import post_model
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

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