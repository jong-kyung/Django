# Django
## Django 특징
- 풀스택 프레임워크
- 기본 DB : sqlite3
- 신속한 개발
- 클래스 기반 뷰, 함수 기반 뷰 두 방식 모두 유연하게 사용 가능
- 중복되는 코드가 있는경우 Mixin 객체(상속을 목적으로 만드는 객체)를 만들어 상속하여 사용함

## Django 사용법
### Django 프로젝트 생성
``` python
python -m django myproject (프로젝트명) . # Django project 생성

python manage.py migrate

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

## Django 라이브러리
### Django-rest-framework