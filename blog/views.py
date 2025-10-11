from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from .models import Post
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

#function base view show a template.
"""
def indexview(request):
    '''
    a function based view to show index page.
    '''
    name = "ali"
    context={
        "name":name
    }
    return render (request,'index.html',context)
"""
class IndexView(TemplateView):
    """
    a class based view to show index page.
    """
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context
    
"""
FBV for redirect
from django.shortcuts import redirect
def redirectToMaktab(request):
    return redirect('https://maktabkhooneh.com')
"""
class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.com'
    
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post,pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostList(ListView):
    model = Post
    context_object_name = "posts"
    