from django.shortcuts import render
# 각 문제를 해결하기 위하여 필요한 import문은 이곳에 작성합니다.
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from .models import Reservation
from .forms import ReservationForm


def index(request):
    reservations = Reservation.objects.order_by('-date') # date 칼럼 기준 내림차순으로 가져오도록
    context = {
        'reservations':reservations,
    }
    return render(request, 'reservations/index.html', context) # reservations/index.html 렌더

def create(request):
    if request.method == 'POST': # POST 방식
        form = ReservationForm(request.POST) # ReservationForm 활용
        if form.is_valid(): # 유효성 검사
            form.save()
            return redirect('reservations:index') # reservaitons 경로로 리다이렉트
        else:
            messages.info(request, '정확히 입력해주세요')
    else: # GET 방식
        form = ReservationForm() # ReservationForm 활용
    context = {
        'form':form,
    }
    return render(request, 'reservations/create.html', context) # reservations/create.html 렌더