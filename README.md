# Django
## Django 특징
- 풀스택 프레임워크
- 기본 DB : sqlite3
- 신속한 개발
- 클래스 기반 뷰, 함수 기반 뷰 두 방식 모두 유연하게 사용 가능
- 중복되는 코드가 있는경우 Mixin 객체(상속을 목적으로 만드는 객체)를 만들어 상속하여 사용함
- 정규식 표현으로 엄격하게 url 패턴 지정이 가능
- 다양한 포맷의 문자열에 대해서도 템플릿 시스템 기능을 제공(SSR)해줌(ex. Python, Javascript, HTML, CSS 등)

### Django - View
- 뷰에서 모든 처리를 하지말 것
- Model/From/Serializer를 적절히 활용할 것
- view 함수의 첫 번째 인자는 HttpRequest 객체임

## Django 사용법
### Django 프로젝트 생성
``` python
python -m django myproject (프로젝트명) . # Django project 생성

python manage.py migrate # 현 프로젝트에 활성화된 장고앱 내에 미리 정의된 마이그레이션 내역으로 데이터베이스 생성

python manage.py createsuperuser # 슈퍼유저 계정 생성

python manage.py runserver # 서버 실행
```

### Django 앱생성
``` python
python manage.py startapp (앱이름) # 장고앱 생성

# setings.py 
INSTALLED_APPS = [
    ...
    '앱이름1',
    '앱이름2'
] # 여기에 꼭 생성한 앱을 등록해주기
```

### Django models 
``` python
python manage.py makemigrations app # DB에 모델을 생성
python manage.py sqlmigrate app 0002 # 어떤 마이그레이션이 실행될 것 인지 확인
python manage.py showmigrations app # 마이그레이션 적용 내역 확인
python manage.py migrate app # DB에 테이블 추가
```

### Django SQL 쿼리내역 출력
``` python
# settings.py
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
}, },
    "loggers": {
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
}, }
```
### Django 라우팅
``` HTML
<!-- 경로 : 앱이름/templates/앱이름 -->
<HTML> ... </HTML>
```

``` python
# 사용할땐
# app/views.py
def index(request:HttpRequest) -> HttpResponse:
    return render(request, 'app/index.html' )

# mysite/urls.py
urlpatterns = [
    ...
    path('app/', app_views.index),
]
```
### Django urlpatterns
``` python
# mysite/settings
ROOT_URLCONF = 'mysite.urls' # root
urlpatterns = [ # 라우팅페이지
    path('app/', include('app.urls'))
]

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index) # 주소에 매핑, 첫번째 인자로 경로, 두번째 인자로 함수 객체를 넘김
]
```

## Django 라이브러리
### Django-environ
- 환경변수 설정용 라이브러리
- 사용방법
``` python
# .env
EMAIL_HOST = smtp주소
EMAIL_PORT = port번호
EMAIL_USE_SSL = true
EMAIL_HOST_USER = your-id
EMAIL_HOST_PASSWORD = your-pw

# mysite/settings
from environ import Env

env = Env() # env 객체 생성
env_path = BASE_DIR / '.env' # env파일 경로 설정
if env_path.exists():
    with env_path.open('rt', encoding='UTF8') as f:
        env.read_env(f, overwrite = True)
...

# SMTP 설정
EMAIL_HOST = env.str('EMAIL_HOST')
EMAIL_PORT = env.int('EMAIL_PORT')
EMAIL_USE_SSL = env.bool('EMAIL_UST_SSL')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSSWORD')

DEFAULT_FORM_EMAIL = f'{EMAIL_HOST_USER}@naver.com'
```