from django.http import HttpResponse
from django.shortcuts import render

from ..members.models import User


def index(request):
    # 모든 유저의 username, img_profile, nickname을 리스트로 보여주는 뷰 생성
    # 이 뷰에는 새 css를 적용 (bootstrap -> static)
    context = {
        'user_list': User.objects.all()
    }
    return render(request, 'index.html', context)
