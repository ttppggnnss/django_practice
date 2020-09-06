from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm): # 모델 폼 상속받음
    class Meta:
        model = Reservation
        fields = '__all__' # 모든 필드값