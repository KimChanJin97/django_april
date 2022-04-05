from django.urls import path
from . import views 
# Model
# Templates
# Views

# Model 과 Templates 을 이어주는 것이 Views 라면
# Views 와 Templates 을 이어주는 것은 URLconf

# 현재경로가 word_counter 앱 안에 있으니 거기서 views.py 를 모듈로 불러오겠다는 의미

urlpatterns = [
    path("", views.index, name="index"), # https://도메인
    path("result", views.result, name="result"), # https://도메인/result
]
