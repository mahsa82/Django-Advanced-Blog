from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


app_name = 'blog'
urlpatterns =[
    #path("fbv-index/",views.indexview ,name ='fbv-test'),
    #path("cbv-index/", TemplateView.as_view(template_name="index.html",extra_context={"name":"ali"})),
    path('cbv-index/',views.IndexView.as_view(),name='cbv-index'),
    path('post/',views.PostList.as_view(),name='post-list'),
    path("go-to-maktabkhooneh/<int:pk>",views.RedirectToMaktab.as_view(),name="go-to-maktabkhoone"),
    
]