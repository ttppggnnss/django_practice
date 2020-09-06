from django import forms
from .models import Movie, Review, Comment

class ReviewForm(forms.ModelForm):
    rank = forms.DecimalField(
        max_digits=5,
        decimal_places=1,
        max_value=5,
        min_value=0,
        label='평점',
        help_text='0~5점까지 평점을 매겨주세요.',
        widget=forms.TextInput(
            attrs={
                'placeholder': '영화 평점 입력',
                'required':'required',
                'max':'5',
                'min':'0',
            }
        )
    )
    title = forms.CharField(
        max_length=100,
        label='글 제목',
        help_text='제목은 100자이내로 작성하세요.',
        widget=forms.TextInput(
            attrs={
                'placeholder': '리뷰 제목 입력',
                'required':'required',
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
        model = Review
        fields = ['title', 'rank', 'content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                'rows': 1,
                'cols': 50,
                'placeholder':'자유롭게 작성해주세요.'
            }
        )
    )
    class Meta:
        model = Comment
        fields = ['content']