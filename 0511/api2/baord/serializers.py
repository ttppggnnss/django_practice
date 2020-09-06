from rest_framework import serializers
# from django import forms 와 유사
from .models import Article

# class ARticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = '__all__'
        fields = ['title', 'created_at']
