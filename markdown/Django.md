## Django 흐름도
![Django 흐름도](image.png)
* 요청은 URL!
* View가 필요에 따라 분석해서
* HTML로 응답함.

## 프로젝트 시작하기
1. Dajngo 라이브러리 다운
    ```
    $ pip install django
    ```
2. 프로젝트 생성
    ```
    $ django-admin startproject 프로젝트폴더
    $ django-admin startproject 프로젝트폴더. #.은 현재폴더
    # 마스터 폴더가 같이 생긴다.
    ```
    폴더 내부로 들어가서
    ```
    $ cd 프로젝트폴더
    ```
    데이터베이스 생성
    ```
    $ python manage.py migrate
    ```
3. 프로젝트 실행
   ```
   $ python manage.py runserver 
    ```
4. 페이지(앱) 만들기
    ```
    $ python manage.py startapp 앱
    ```
5. 프로젝트에 앱 등록
   1. `settings.py`의 INSTALLED_APPS에 `앱` 추가
    ```
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '앱',
    ]
    ```
6. html 만들기
   1. 프로젝트폴더/앱/templates(폴더생성)/함수명.html 생성
   2. 함수명.html > ! + tab
     ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        홈페이지
    </body>
    </html>
   ```
7. `앱/views.py`에 함수 추가
    ```
    from django.shortcuts import render
    
    def 함수명(request):
        return render(request,'앱/함수명.html')

    ```
8. `앱/view.py`와 `앱/urls.py(생성)` 연결
    ```
    from django.urls import path
    from . import views  #.은 현재폴더
    
    urlpatterns = [
        path('', views.함수명),
    ]
    ```
9. `앱 url`와 `프로젝트 url` 연결
    * `프로젝트폴더/urls.py` 에서
    ```
    from django.contrib import admin
    from django.urls import path, include
    # include를 통해서 앱 url 연결

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('앱.urls')),
    ]
    ```

## Base.html 연결하기
> Base.html 이용하여 중복부분 제거 가능
1. 프로젝트폴더/templates/base.html 생성
2. base.htm > ! + tab > 중복내용 방지 위치에 `{% block content %} {% endblock content %}` 삽입
3. 

## DB
> 과정 : python > ORM(object relational mapper) > SQL
* 프로젝트폴더/앱/models.py
* ~~프로젝트폴더/settings.py > INSTALLED_APPS <앱이름> 등록~~
* 테이블 만들기 > 테이블 변수 종류 명확히 표시 예)integer, Float 등
```
# 1차 시안 개념

from django.db import models

class Student(models.Model): # 테이블명
    # 컬럼 명 = 데이터 타입
    # charfield만 길이값 삽입
    name = models.CharField(max_length=10)
    address = models.TextField()
    major = models.CharField(max_length=100)
    age = models.IntegerField()
    cpga = models.FloatField()
```
* `$ python manage.py makemigrations <앱이름>` : 최종 시안 개념
* `$ python manage.py migrate <앱이름>` > db.sqlite3 > 빈 테이블 생성
* 수정 시 : models.py 수정 > makemigrations > migrate 





## 재정리 필요
* python manage.py runserver # 서버 구동
* python manage.py startapp first_app # 프로젝트 생성
* settings > INSTALLED_APPS = > 'first_app', #프로젝트 등록(출생신고?)
* urls.py > urlpatterns = path('URL/', 함수명.urls), # URL,함수명 지정
* 프로젝트 폴더 > View 함수 > templates에 def 생성

리뷰 urls.py 만들기

```
def 함수이름(request) context={} return render(request, 'html', context) 
```


$ cd user_input
$ mkdir -p templates/userinput

form > path('user_input/', include('user_input.urls')),
user_input > urls.py
views.py > def 선언
templates/앱폴더 > hello.html


hello/<str:name>/', views.hello


## 23-10-04
* if __name__ == '__main__':
    print('내가 부르는 이름)

## 자료 입력
1. python manage.py shell
```
이하 객체

from students.models import Student
s= Student()
s.name = '김학생'
~
s.age = 25
s.save() > 객체 > DB 저장 매서드
```

Student.objects.create(
    name='박학생'
)

Student.objects.get(id==pk=1) #Primary key 