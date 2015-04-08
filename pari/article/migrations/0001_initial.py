# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pari.article.managers
import mezzanine.core.managers
import geoposition.fields
from django.conf import settings
import mezzanine.core.fields
import pari.article.mixins.admin_thumb


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments_count', models.IntegerField(default=0, editable=False)),
                ('keywords_string', models.CharField(max_length=500, editable=False, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('_meta_title', models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', blank=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('strap', models.CharField(max_length=600, null=True, blank=True)),
                ('is_topic', models.BooleanField(default=False, verbose_name='Is a topic?')),
                ('allow_comments', models.BooleanField(default=False, verbose_name='Allow comments')),
                ('allow_featured_image', models.BooleanField(default=False, verbose_name='Show Featured Image for the Article')),
                ('featured_image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Featured Image', blank=True)),
                ('featured_image_caption', models.CharField(max_length=1000, null=True, blank=True)),
                ('pin_to_home', models.BooleanField(default=False, verbose_name='Pin to home?')),
                ('carousel_order', models.SmallIntegerField(null=True, verbose_name='Carousel order', blank=True)),
                ('capsule_video', models.CharField(max_length=100, null=True, blank=True)),
                ('featured_video', models.URLField(null=True, blank=True)),
                ('featured_audio', models.URLField(null=True, blank=True)),
                ('date_of_publication', models.DateField(null=True, verbose_name='Original date of publication', blank=True)),
                ('oembed_data', models.TextField(default=b'{}', null=True, blank=True)),
            ],
            options={
                'ordering': ('-publish_date',),
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model, pari.article.mixins.admin_thumb.AdminThumbMixin),
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
                (b'articles', pari.article.managers.ArticleManager()),
                (b'topics', pari.article.managers.TopicManager()),
            ],
        ),
        migrations.CreateModel(
            name='ArticleCarouselImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords_string', models.CharField(max_length=500, editable=False, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('_meta_title', models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', blank=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('file', mezzanine.core.fields.FileField(max_length=200, verbose_name='File')),
                ('article', models.ForeignKey(related_name='carousel_images', to='article.Article')),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'CarouselImage',
                'verbose_name_plural': 'CarouselImages',
            },
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords_string', models.CharField(max_length=500, editable=False, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('_meta_title', models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', blank=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('twitter_username', models.CharField(max_length=50, null=True, blank=True)),
                ('facebook_username', models.CharField(max_length=50, null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name="Author's Image", blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords_string', models.CharField(max_length=500, editable=False, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('_meta_title', models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', blank=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('image', mezzanine.core.fields.FileField(max_length=255, verbose_name='Image', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('_order', 'title'),
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model, pari.article.mixins.admin_thumb.AdminThumbMixin),
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords_string', models.CharField(max_length=500, editable=False, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('_meta_title', models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', blank=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('location', geoposition.fields.GeopositionField(max_length=42, verbose_name=b'Location')),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=5)),
                ('icon_class', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(related_name='articles', verbose_name=b'Author', to='article.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='category_list',
            field=models.ManyToManyField(related_name='articles', verbose_name='Categories', to='article.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='locations',
            field=models.ManyToManyField(to='article.Location', verbose_name='Locations', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='related_posts',
            field=models.ManyToManyField(related_name='related_posts_rel_+', verbose_name='Related Articles', to='article.Article', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='site',
            field=models.ForeignKey(editable=False, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='article',
            name='types',
            field=models.ManyToManyField(related_name='articles', verbose_name=b'Article Type', to='article.Type'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(related_name='articles', verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),
    ]
