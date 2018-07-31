
from django.contrib import admin
from django.urls import path,include
from moviesapp.views import MoviesList,CommentsList,AddTitle,AddComment
from rest_framework import routers


router=routers.DefaultRouter()
router.register('all_movies',MoviesList,base_name='MoviesList',)
router.register('all_comments',CommentsList,base_name='CommentsList',)
router.register('add_comment',AddComment,base_name='AddComment',)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('root/',include(router.urls)),
    path('root/add_title/', AddTitle.as_view(), name='add_title'),

]
