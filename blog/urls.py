## Create app-specific URL:
# blog/urls.py
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    # map the URL (empty string) to the view
    path('', RandomArticleView.as_view(), name='random'), ## new
    path('show_all', ShowAllView.as_view(), name='show_all_articles'), ## refactored
    path('article/<int:pk>', ArticleView.as_view(), name='article'), # show one article
    path('article/<int:pk>/create_comment', CreateCommentView.as_view(), name='create_comment'), ##With PK
    path('create_article', CreateArticleView.as_view(), name='create_article'),  ### NEW
    path('article/<int:pk>/update', UpdateArticleView.as_view(), name="update_article"), # NEW
    path('delete_comment/<int:pk>', DeleteCommentView.as_view(), name='delete_comment'),
]