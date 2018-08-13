from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from moviesapp.views import *


router = routers.DefaultRouter()
router.register('all_movies', MoviesList, base_name='MoviesList',)
router.register('all_comments', CommentsList, base_name='CommentsList',)
router.register('add_comment', AddComment, base_name='AddComment',)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('root/', include(router.urls)),
    path('root/add_title/', AddTitle.as_view(), name='add_title'),

]
