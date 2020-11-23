from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView,
UpdateView,
DeleteView,
CreateView,
DetailView)
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Post

User = get_user_model()
# Here we are creating the views and tell django what we want to show in the url that we set on the urls.py file
# Each view here will get a request and will return what we want to render
# We need to return in the render function the request, the html file in our templates folder, and some data we want to give the 
# html to show in a form of dictionary
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})


# These are class based views, they will inherit from django classes and will have a lot of logic already in them (Like forms, redirects, etc)
# We need to set the model to the model that we want to work with
# By default class based view will pass and look for the word "object" when interacting with the html files
# Unless we change the default like in the PostListView 
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 5 #The Paginate object is already in the ListView class so we can just set the attrebute

#This class will make us see only the posts created by a specific user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5 

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) #This will get the user from the URL or a 404 if not existed
        return Post.objects.filter(author=user).order_by('-id')

class PostDetailView(DetailView):
    model = Post

# Here we set the form when creating a new post
# We use the LoginRequiredMixin to make sure you can only create a post if the user is logged in
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    
    # We let django know that the form author is the logged in user and save the new post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# We set the model to be the Post and the form fields to edit the Post
# We use these mixins to make sure that you can only edit the post if you are logged in, and logged in as the author of the post 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ['title', 'content']

    # Led django know who is the author of the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #get the post, and check if the author is the logged in user 
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

#Set the model to be a Post and sets the redirect view to be the home page 
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'