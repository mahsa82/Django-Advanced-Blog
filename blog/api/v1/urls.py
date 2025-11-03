from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")

app_name = "api-v1"

urlpatterns = router.urls

# urlpatterns = [
#      path('post/',views.PostList, name="post-list"),
#      path('post/<int:id>/',views.postDetail , name="post-detail"),
#      path('post/',views.PostList.as_view() , name="post-list"),
#      path('post/<int:pk>/',views.PostDetail.as_view() , name="post-detail"),
#      path('post/',views.PostViewSet.as_view({'get':'list','post':'create'}),name='post-list'),
#      path('post/<int:pk>/',views.PostViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='post-list'),
#      path('',include(router.urls)),
# ]
# urlpatterns += router.urls
