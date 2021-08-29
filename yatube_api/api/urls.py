from django.urls import path, include
from rest_framework import routers

from . import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts',
                   views.PostViewSet, basename='posts')
router_v1.register(r'groups',
                   views.GroupViewSet, basename='groups')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   views.CommentViewSet, basename='comments')
router_v1.register(r'follow',
                   views.FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
