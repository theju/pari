from django import forms
from pari.news.models import NewsPost, NewsCategory, LatestArticle


class NewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        exclude = ()


class NewsCategoryForm(forms.ModelForm):
    class Meta:
        model = NewsCategory
        exclude = ()


class LatestArticleForm(forms.ModelForm):
    class Meta:
        model = LatestArticle
        exclude = ()
