# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.managers
import mezzanine.core.fields
import pari.article.mixins.admin_thumb


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factoid',
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
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True)),
                ('external_link', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'verbose_name': 'Factoid',
                'verbose_name_plural': 'Factoids',
            },
            bases=(models.Model, pari.article.mixins.admin_thumb.AdminThumbMixin),
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
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
                ('embed_source', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=100, null=True, blank=True)),
                ('authors', models.TextField(max_length=200, null=True, verbose_name='Author', blank=True)),
                ('focus', models.TextField(max_length=1000, null=True, verbose_name='Focus', blank=True)),
                ('copyright', models.TextField(max_length=200, null=True, verbose_name='Copyright', blank=True)),
                ('thumbnail_url', models.TextField(help_text=b'Non editable field which will be auto-populated based on embed source', null=True, blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
            },
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
        migrations.AddField(
            model_name='factoid',
            name='resource',
            field=models.ForeignKey(related_name='factoids', blank=True, to='resources.Resource', null=True),
        ),
        migrations.AddField(
            model_name='factoid',
            name='site',
            field=models.ForeignKey(editable=False, to='sites.Site'),
        ),
    ]
