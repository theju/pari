# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.managers
from django.conf import settings
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('new_archive_articles', models.ManyToManyField(related_name='new_archive_articles', verbose_name='New archive articles', to='article.Article', blank=True)),
                ('new_current_articles', models.ManyToManyField(related_name='new_current_articles', verbose_name='New current articles', to='article.Article', blank=True)),
            ],
            options={
                'verbose_name': 'Latest article',
                'verbose_name_plural': 'Latest articles',
            },
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'News Category',
                'verbose_name_plural': 'News Categories',
            },
            managers=[
                (b'objects', mezzanine.core.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='NewsPost',
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
                ('allow_comments', models.BooleanField(default=False, verbose_name='Allow comments')),
                ('categories', models.ManyToManyField(related_name='news_posts', verbose_name='News Category', to='news.NewsCategory', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
                ('user', models.ForeignKey(related_name='newsposts', verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish_date',),
                'verbose_name': 'News post',
                'verbose_name_plural': 'News posts',
            },
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
    ]
