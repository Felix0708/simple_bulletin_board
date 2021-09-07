from django import forms
from django.forms.widgets import TextInput, Textarea
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '제목을 입력하세요.',
                'maxlength': 20,
                'style' : 'border: solid 2px gray; border-radius: 8px; width: 25rem;'
            }
        ),
        error_messages={
            'required': '(공백 X, 제목을 입력하세요.)',
        },
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': '내용을 입력하세요.',
                'rows': 5,
                'cols': 52,
                'style': 'border: solid 2px gray; border-radius: 8px;'
            }
        ),
        error_messages={
            'required': '(공백 X, 내용을 입력하세요.)'
        },
    )

    class Meta:
        model = Article
        fields =  ('title', 'content',)
