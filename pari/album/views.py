from django.views.generic import DetailView, ListView
from pari.album.models import Album, AlbumImage, ImageCollectionImage

import json
from django.http import HttpResponse
from django.contrib.sites.models import RequestSite
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

from mezzanine.conf import settings


class AlbumList(ListView):
    model = Album

    def get_context_data(self, *args, **kwargs):
        context = super(AlbumList, self).get_context_data(*args, **kwargs)
        context['albums'] = self.kwargs['albums']()
        return context


class AlbumDetail(DetailView):
    context_object_name = "album"
    model = Album


class AlbumImageDetail(DetailView):
    context_object_name = "image"
    model = AlbumImage

    def get_object(self, queryset=None):
        return AlbumImage.objects.get(album__slug=self.kwargs['slug'],
                                      _order=int(self.kwargs['order']) - 1)


class ImageCollectionImageList(DetailView):
    context_object_name= "image_collection"
    model = ImageCollectionImage

    def get_object(self, queryset=None):
        album = Album.objects.get(slug=self.kwargs['slug'])
        return album.image_collection.images


def embed_talking_album(request):
    url = request.GET.get("url")
    # http://www.ruralindiaonline.org/albums/the-green-army/
    slug = filter(lambda x: x, url.split("/"))[-1]
    album = Album.objects.get(slug=slug)
    is_request_secure = request.is_secure()
    domain = RequestSite(request).domain
    album_embed_url = "http{0}://{1}{2}".format(
        "s" if is_request_secure else "",
        domain,
        reverse("embed-talking-album-detail", kwargs={"id": album.id})
    )
    author_url = "http{0}://{1}".format(
        "s" if is_request_secure else "",
        domain,
        album.photographer.get_absolute_url()
    )
    width = request.GET.get("width", "1024")
    height = request.GET.get("height", "768")
    response = json.dumps({
        "type": "rich",
        "version": 1.0,
        "title": album.title,
        "author_name": album.photographer.title,
        "author_url": author_url,
        "provider_name": settings.SITE_FULL_TITLE,
        "provider_url": "http{0}://{1}/".format(
            "s" if is_request_secure else "",
            domain
        ),
        "html": """<iframe src="{0}" width="{1}" height="{2}"></iframe>""".format(
            album_embed_url,
            width, height
        ),
        "width": width,
        "height": height
    })
    content_type = "application/json"
    if request.GET.get("callback"):
        response = "{0}({1})".format(request.GET["callback"], response)
        content_type = "application/javascript"
    return HttpResponse(response, content_type=content_type)


def embed_talking_album_detail(request, id=None):
    album = get_object_or_404(Album, id=id)
    return render(request, "album/album_detail.html", {
        "album": album,
        "embed": True
    })
