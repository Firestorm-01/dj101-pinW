
from django.views.generic import TemplateView, DetailView,FormView
from .models import Post
from  .forms import PostForm
from  django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
class HomePageView(TemplateView):
   template_name="home.html"
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context

class PostDetailView(DetailView):
   template_name="detail.html"
   model=Post

class AddPostView(FormView):
    template_name = "newpost.html"
    form_class = PostForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to add a post.')
            return redirect('feed:index')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        text = form.cleaned_data['text']
        image = form.cleaned_data.get('image')
        file = form.cleaned_data.get('file')
        Post.objects.create(text=text, image=image, file=file)
        messages.success(self.request, 'Post created successfully!')
        return super().form_valid(form)
