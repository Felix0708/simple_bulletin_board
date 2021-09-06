from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        fields =  ('title', 'content', 'img_path')