from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=20,
        label='제목',
        help_text='제목은 20자이내로 작성하세요.',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목 입력'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        help_text='자유롭게 작성해주세요.',
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'cols': 50,
            }
        )
    )
    class Meta:
        model = Article
        # fields = ['title', 'content']
        fields = '__all__'