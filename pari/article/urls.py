from django.conf.urls import patterns, url

from .views import (LocationDetail, CategoriesList, CategoryDetail, ArticleDetail,
                    ArticleList, KeywordDetail, AuthorDetail, ArchiveDetail, ArticleCarouselImageDetail)

urlpatterns = patterns('pari.article.views',
    url(r'^categories/(?P<slug>.+)/$', CategoryDetail.as_view(), name='category-detail'),
    url(r'^categories/$', CategoriesList.as_view(), name='category-list'),
    url(r'^authors/(?P<slug>.+)/$', AuthorDetail.as_view(), name='author-detail'),
    url(r'^articles/(?P<slug>.+)/$', ArticleDetail.as_view(), name='article-detail'),
    url(r'^articles/(?P<slug>.+)/(?P<order>\d+)/$', ArticleCarouselImageDetail.as_view(), name='article-image-detail'),
    url(r'^articles/$', ArticleList.as_view(), name='article-list'),
    url(r'^topics/(?P<slug>.+)/$', AuthorDetail.as_view(), name='topic-detail'),
    url(r'^locations/(?P<slug>.+)/$', LocationDetail.as_view(), name='location-detail'),
    url(r'^keywords/(?P<slug>.+)/$', KeywordDetail.as_view(template_name="article/keyword_detail.html"), name='keyword-detail'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d+)/$', ArchiveDetail.as_view(), name='archive-detail'),
)
