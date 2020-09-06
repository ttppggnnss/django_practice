from django import forms
from .models import Issue, Reply

class IssueForm(forms.ModelForm):
    nameA = forms.CharField(
        max_length=20,
        label='',
        help_text='20자로 제한됩니다.',
        widget=forms.TextInput(
            attrs={
                'placeholder': '비교대상 1 입력',
                'required':'required',
                'autofocus':'autofocus',
            }
        )
    )
    nameB = forms.CharField(
        max_length=20,
        label='',
        help_text='20자로 제한됩니다.',
        widget=forms.TextInput(
            attrs={
                'placeholder': '비교대상 2 입력',
                'required':'required',
            }
        )
    )
    class Meta:
        model = Issue
        fields = ['nameA','nameB']


CHOICES=[('A','A'),('B','B')]
class ReplyForm(forms.ModelForm):
    pick = forms.ChoiceField(
        label='',
        choices=CHOICES,
        widget=forms.RadioSelect(
            attrs={
                'class':"radio-inline"
            }
        )
    )
    comment = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder':'자유롭게 작성해주세요.'
            }
        )
    )
    class Meta:
        model = Reply
        fields = ['pick','comment']