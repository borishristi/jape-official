from django.urls import path
from .views import index_view, article_view, template_view


urlpatterns = [
    # path('', index_view, name='blog-index_view'),
    path('article-<str:numero_article>/', article_view, name='blog-article'),
    path('', template_view, name='template_view')
]