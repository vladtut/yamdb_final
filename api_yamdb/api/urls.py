
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserAdminViewSet,
                    get_jwt_token, user_signup)

router = DefaultRouter()
router.register(r'users', UserAdminViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments',
)
urlpatterns_auth = [
    path('auth/signup/', user_signup, name='signup'),
    path('auth/token/', get_jwt_token, name='token')
]
app_name = 'api'

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(urlpatterns_auth)),
]
