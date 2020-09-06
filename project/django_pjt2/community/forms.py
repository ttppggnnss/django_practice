from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    movie_title = forms.CharField(
        max_length=30,
        label='영화 제목',
        help_text='영화 제목은 30자로 제한됩니다.',
        widget=forms.TextInput(
            attrs={
                'placeholder': '영화 제목 입력',
                'required':'required',
                'autofocus':'autofocus',
            }
        )
    )
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
    reviewer = forms.CharField(
        max_length=10,
        label='작성자',
        help_text='최대 10자로 제한됩니다.',
        widget=forms.TextInput(
            attrs={
                'placeholder': '작성자',
                'required':'required',
            }
        )
    )
    password = forms.CharField(
        label='비밀번호',
        help_text='삭제 및 수정에 필요합니다.',
        widget=forms.TextInput(
            attrs={
                'type':'password',
                'required':'required',
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
    hitcount = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class':'d-none',
                'value':'0',
            }
        )
    )

    class Meta:
        model = Review
        fields = '__all__'