from django import forms
from .models import About, Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image","article_category","is_superarticle"]

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ["content"]