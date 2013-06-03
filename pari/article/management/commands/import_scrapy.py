from optparse import make_option
import json
from datetime import datetime

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from mezzanine.generic.models import Keyword, AssignedKeyword

from pari.article.models import Article, Author, Type, Location


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("-f", "--filename",
                action="store", type="string", dest="filename"),
        )

    def handle(self, *args, **options):
        jsonfilename = options['filename']
        with open(jsonfilename, 'r') as f:
            for line in f:
                jsoncontent = json.loads(line)
                title = jsoncontent['title'][0].encode('utf-8').strip()
                try:
                    new_article = Article.objects.get(title=title)
                    type_of_import = "Update"
                except ObjectDoesNotExist:
                    new_article = Article()
                    new_article.title = title
                    type_of_import = "Update"
                print "{0} {1}".format(type_of_import, title)
                
                try:
                    author=Author.objects.get(title=jsoncontent['author'][0])
                except ObjectDoesNotExist:
                    author = Author(title=jsoncontent['author'][0])
                    author.save()
                new_article.author = author

                new_article.user = User.objects.get(pk=1)
                new_article.content = jsoncontent['content']
                new_article.publish_date = datetime.strptime(jsoncontent['date'], "%B %d, %Y").replace(tzinfo=timezone.utc)

                new_article.save()

                new_article.types.add(Type.objects.get(title='Photo'))

                location_name = jsoncontent['location'].strip(',\n')
                try:
                    location = Location.objects.get(title__iexact=location_name)
                    new_article.locations.add(location)
                except ObjectDoesNotExist:
                    pass

                for k in jsoncontent['keywords']:
                    try:
                        keyword = Keyword.objects.get(title=k)
                    except ObjectDoesNotExist:
                        keyword = Keyword(title=k)
                        keyword.save()

                    if not new_article.keywords.filter(keyword=keyword).exists():
                        new_article.keywords.add(AssignedKeyword(keyword=keyword))
