# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.managers
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
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
                ('zip_import', models.FileField(help_text="Upload a zip file containing images, and they'll be imported into this gallery.", upload_to=b'albums', verbose_name='Zip import', blank=True)),
                ('meta_data', models.CharField(max_length=200, verbose_name='About the album', blank=True)),
                ('predominant_tone', models.CharField(default=b'colour', max_length=10, choices=[(b'grey', b'Greyscale'), (b'colour', b'Colour')])),
                ('articles', models.ManyToManyField(to='article.Article', blank=True)),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
        migrations.CreateModel(
            name='AlbumImage',
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
                ('audio', models.CharField(max_length=30, null=True, blank=True)),
                ('audio_file', models.FileField(max_length=200, upload_to=b'albums', null=True, verbose_name='File', blank=True)),
                ('is_cover', models.BooleanField(default=False, verbose_name=b'Album cover')),
                ('image_file', mezzanine.core.fields.FileField(max_length=200, null=True, verbose_name='File')),
                ('album', models.ForeignKey(related_name='images', to='album.Album')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'AlbumImage',
                'verbose_name_plural': 'AlbumImages',
            },
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
        migrations.CreateModel(
            name='ImageCollection',
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
                ('zip_import', models.FileField(help_text="Upload a zip file containing images, and they'll be imported into this collection.", upload_to=b'albums', verbose_name='Zip import', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Image Collection',
                'verbose_name_plural': 'Image Collection',
            },
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
        migrations.CreateModel(
            name='ImageCollectionImage',
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
                ('image_collection', models.ForeignKey(related_name='images', to='album.ImageCollection')),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'ImageCollectionImage',
                'verbose_name_plural': 'ImageCollectionImages',
            },
            managers=[
                (b'objects', mezzanine.core.managers.DisplayableManager()),
            ],
        ),
        migrations.AddField(
            model_name='albumimage',
            name='image_collection_image',
            field=models.ForeignKey(related_name='album_image', to='album.ImageCollectionImage'),
        ),
        migrations.AddField(
            model_name='albumimage',
            name='location',
            field=models.ForeignKey(verbose_name='Location', to='article.Location'),
        ),
        migrations.AddField(
            model_name='albumimage',
            name='photographer',
            field=models.ForeignKey(related_name='photographs', to='article.Author'),
        ),
        migrations.AddField(
            model_name='albumimage',
            name='site',
            field=models.ForeignKey(editable=False, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='album',
            name='image_collection',
            field=models.ForeignKey(to='album.ImageCollection'),
        ),
        migrations.AddField(
            model_name='album',
            name='location',
            field=models.ForeignKey(related_name='albums', blank=True, to='article.Location', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='photographer',
            field=models.ForeignKey(related_name='albums', blank=True, to='article.Author', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='site',
            field=models.ForeignKey(editable=False, to='sites.Site'),
        ),
    ]
