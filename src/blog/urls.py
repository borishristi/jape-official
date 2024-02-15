from django.conf.urls.static import static
from django.urls import path

from jape_official import settings
from .views import index_view, article_view, template_view, test_design_view


urlpatterns = [
    # path('', index_view, name='blog-index_view'),
    path('article-<str:numero_article>/', article_view, name='blog-article'),
    path('', template_view, name='template_view'),
    path('test_design/', test_design_view, name='test_design_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)