from django.urls import path
from .views import weather  # weather 뷰를 가져옵니다.

urlpatterns = [
    path('', lambda request: redirect('weather/', permanent=True)),  # 루트 URL을 weather/로 리디렉션
    path('weather/', weather, name='weather'),  # /weather/ URL에 대한 뷰를 설정합니다.
    # 다른 URL 패턴들을 추가할 수 있습니다.
]
