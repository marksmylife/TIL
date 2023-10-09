## Django 흐름도
![Alt text](%EC%9E%A5%EA%B3%A0%ED%9D%90%EB%A6%84%EB%8F%84-1.JPG)
* 요청은 URL!
* View가 필요에 따라 분석해서
* HTML로 응답함.
* prject urls.py > app urls.py > view.def 


## C R U D
1. <프로젝트> 생성
    ```
    django-admin startproject <프로젝트>
    ```
2. <앱> 생성
    ```python
    python manage.py startapp <앱>
    ```
3. <프로젝트> 폴더 → setting.py
    ```python
   INSTALLED_APPS = [
    '<앱>',
    ]
    ```
4. migrate 실행
    ```python
    python manage.py makemigrations <앱> : 최종 시안 개념
    python manage.py migrate <앱> > db.sqlite3 > 빈 테이블 생성
    ```
5. <프로젝트> 폴더 → urls.py
    ```python
    from django.urls import path, **include**

    urlpatterns = [
        path('<도메인>/', include('<앱>.urls')),
    ]
    ```
6. <앱> 폴더 → urls.py 생성
    ```python
    from django.urls import path
    from . import views
    
    # URL을 변수로 사용하기 => app_name:name 
    app_name = 'crud'
    
    urlpatterns = [
        # /univ/new/
        path('new/', views.new, name='new'),  # crud:new
        # /univ/create/
        path('create/', views.create, name='create'),  # crud:create
        # /univ/
        path('', views.index, name='index'),  # crud:index
        # /univ/1/
        path('<int:pk>/', views.detail, name='detail'),  # crud:detail
        # /univ/1/edit/
        path('<int:pk>/edit/', views.edit, name='edit'),  # crud:edit
        # /univ/1/update/
        path('<int:pk>/update/', views.update, name='update'),  # crud:update
        # /univ/1/delete/
        path('<int:pk>/delete/', views.delete, name='delete'),  # crud:delete
    ]
    ```
7. <앱> 폴더 > views.py 함수 생성
    ```python
    from django.shortcuts import render, redirect
    from .models import Student

    def new(request):
        # 새로운 student 를 생성하기 위한 <form>(HTML) => 작성데이터는 create 함수로 보내야 함
        return render(request, 'crud/new.html')

    def create(request):
        # new.html 에서 넘어온 데이터를 실제 저장
        student = Student()
        student.name = request.GET['student_name']
        student.age = request.GET['student_age']
        student.major = request.GET['student_major']
        student.description = request.GET['student_description']
        student.save()  # 저장 됨! => id(pk)가 생김

        return redirect('crud:detail', student.pk)
        # return redirect(f'/school/{student.pk}/')

    def index(request):
        # 전체 학생 목록 확인
        students = Student.objects.all()
        return render(request, 'crud/index.html', {
            'students': students,
        })

    def detail(request, pk):
        # 학생 상세 정보 확인
        student = Student.objects.get(pk=pk)
        return render(request, 'crud/detail.html', {
            'student': student,
        })

    def edit(request, pk):
        # student 를 수정하기 위한 <form>(HTML) => 작성데이터는 update 함수로 보내야 함
        student = Student.objects.get(pk=pk)
        return render(request, 'crud/edit.html', {
            'student': student,
        })

    def update(request, pk):
        # edit.html 에서 넘어온 데이터를 실제 저장
        student = Student.objects.get(pk=pk)
        student.name = request.GET['student_name']
        student.age = request.GET['student_age']
        student.major = request.GET['student_major']
        student.description = request.GET['student_description']
        student.save() 
        return redirect('crud:detail', student.pk)

    def delete(request, pk):
        # URL 에 넘어온 pk 에 해당하는 학생정보 삭제
        student = Student.objects.get(pk=pk)
        student.delete()
        # view 에서 redirect => '<app_name>:<name>'
        return redirect('crud:index')

        # DTL(템플릿)  {% url '<app_name>:<name>' %}
    ```
8. <프로젝트> 폴더 > templates 폴더 생성 > base.html 생성
    ```python
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
    
      <nav>
        <ul>
          <li>
            <a href="{% url "crud:index" %}">Index</a>
          </li>
          <li>
            <a href="{% url "crud:new" %}">New</a>
          </li>
        </ul>
      </nav>
    
        {% block content %}{% endblock content %}
    </body>
    </html>
    ```
9. <앱> > templates 폴더 생성 > <앱> 폴더 생성 > html 생성
---
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
    $ django-admin startapp <app>
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
2-7. `앱/views.py`에 함수 추가
    ```
    from django.shortcuts import render
    
    def 함수명(request, id):
        return render(request,'앱/함수명.html')
        return HttpResponse('앱' + id)

    ```
3- 1. `앱/view.py`와 `앱/urls.py(생성)` 연결
    ```
    from django.urls import path
    from . import views  #.은 현재폴더
    
    urlpatterns = [
        path('<>', views.함수명),
    ]
    * <> : 변수값 
    ```
1-9. `앱 url`와 `프로젝트 url` 연결
    * `프로젝트폴더/urls.py` 에서
    ```
    from django.contrib import admin
    from django.urls import path, **include**
    # **include**를 통해서 앱 url 연결

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('주소', include('위임app.urls')),
    ]
    ```
    * 프로젝트 urls.py를 위임app에도 복사
```
from django.urls import path
urlpatterns = [
   
]
```

프로젝트urls 내용 넣고 > 복사해서 앱urls 만들고 > 앱 view에 함수만들고 > 앱 urls랑 view 연결하고

### 라우팅
프로젝트urls의 path 주소 > 앱urls path 주소 > 앱view 함수 > 표현

### CRUD
Create Read Updatd Delete

## Base.html 연결하기
> Base.html 이용하여 중복부분 제거 가능
1. 프로젝트폴더/templates/base.html 생성
2. base.htm > ! + tab > 중복내용 방지 위치에 `{% block content %} {% endblock content %}` 삽입
   

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
---

`python manage.py <command>`

`python manage.py runserver (Port.no)` : 서버 실행(취소 : ctrl + c)



---
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

* Student.objects.get(id==pk=1) #Primary key 
* label for, id 와 name은 다름 / 서버측에선 name을 받음

23-10-05
1. 프로젝트/마스터 urls.py에 path 작성(board)
2. 탬플릿/보드 폴더 내에 html 생성
3. 프로젝트/앱/urls.py에 path 작성
4. view.py에서 함수 정의
5. 셋팅 >'DIRS': [BASE_DIR / 'templates'],
6. 마스터 템플릿폴더생성 > base.html 생성


23-10-06
1. models.py에 Class 생성
2. urls.py에 path 작성
3. views.py
4. 탬플릿
5. 각 html 작성
![Alt text](image-1.png)

* 중복방지 : name