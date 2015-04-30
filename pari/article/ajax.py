from django.template.loader import render_to_string

from mezzanine.generic.models import Keyword

from pari.search.models import get_search_results

from .models import (Category, Type, Location, Author,
                     get_category_articles, get_location_articles, get_keyword_articles,
                     get_author_articles, get_archive_articles, get_all_articles)
from .common import get_article_list, get_result_types
from .templatetags.article_filters import month_name


def all_article_filter(request, filter=None, page=1):
    article_queryset = get_all_articles()

    return article_filter(article_queryset, None, filter, page, request)


def category_article_filter(request, category, filter=None, page=1):
    category = Category.objects.get(pk=category)
    article_queryset = get_category_articles(category)

    return article_filter(article_queryset, None, filter, page, request)


def author_article_filter(request, author, filter=None, page=1):
    author = Author.objects.get(pk=author)
    article_queryset = get_author_articles(author)

    return article_filter(article_queryset, None, filter, page, request)


def location_article_filter(request, location, filter=None, page=1):
    location = Location.objects.get(pk=location)
    article_queryset = get_location_articles(location)

    return article_filter(article_queryset, location.title, filter, page, request)


def keyword_article_filter(request, keyword, filter=None, page=1):
    keyword = Keyword.objects.get(pk=keyword)
    article_queryset = get_keyword_articles(keyword)

    return article_filter(article_queryset, keyword.title, filter, page, request)


def archive_article_filter(request, month, year, filter=None, page=1):
    article_queryset = get_archive_articles(month, year)

    return article_filter(article_queryset, "{0} {1}".format(month_name(month), year), filter, page, request)


def search_filter(request, query, filter=None, page=1):
    results = get_search_results(query, filter, page)

    result_types = get_result_types(filter)

    return render_to_string('search/includes/search_result_list.html', {'results': results,
                                                                        'query': query,
                                                                        'filter': filter,
                                                                        'result_types': result_types,
                                                                        'request': request})


def article_filter(article_queryset, title, filter, page, request):
    articles = get_article_list(article_queryset, page, filter)

    return render_to_string('article/includes/article_list.html', {'articles': articles,
                                                                   'title': title,
                                                                   'filter': filter,
                                                                   'types': Type.objects.all(),
                                                                   'request': request})
