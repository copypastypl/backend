from django.urls import path, include
from rest_framework_nested import routers

from . import views

router = routers.SimpleRouter()
router.register('posts', views.PostView, basename='posts')

domains_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
domains_router.register(r'comments', views.CommentView, basename='post-comments')

urlpatterns = [
    path('tags/', views.TagView.as_view(), name='tags'),
    path('', include(router.urls)),
    path('', include(domains_router.urls)),
]
