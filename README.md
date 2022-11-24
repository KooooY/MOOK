# Movie Network, MOOK!

## 목차
1. Description
2. Get Started
3. OverView
4. Development
5. Schedule
6. Languages and Tools
7. ERD
8. Members
9. RetroSpective

<hr>

### Description
<br>

나와 같은 취향을 가진 무비메이트를 찾는 Movie Network, MOOK!
- 영화 감상 공유 SNS 컨셉으로, 내 취향과 감상을 전시하고 나와 유사한 감성의 유저를 찾아 ‘무비메이트’를 만들고 교류하는 것이 목적
- 가입 시 등록한 선호 장르 기반으로 영화를 추천하고, 해당 영화의 리뷰를 통해 나와 유사한 취향과 가치관을 가진 유저를 찾을 수 있는 서비스
- 팔로우, 댓글, 방명록 등 유저 간 교류할 수 있는 다양한 시스템

<hr>

### Get Start
<br>

- client
```
$ git clone 깃주소
$ cd final-pjt-front
$ npm i
$ npm run serve
```
<br>

- server
```
$ git clone 깃주소
$ cd final-pjt-back
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt

$ python manage.py makemigrations
$ python manage.py miragte

# tmdb 기반 영화 데이터 추가
$ python manage.py loaddata genres.json movies.json

# 서버 실행
$ python manage.py runserver
```
<hr>

### Overview
1. 가입하지 않아도 제공되는 랜덤추천기능  
(메인이미지삽입)
- 가입하지 않아도 서비스를 일부 체험해 볼 수 있도록 구성
- 추천영화는 볼 수 있되 리뷰 열람 등의 서비스는 제한하여 가입을 유도

2. 로그인/회원가입  
(이미지삽입)
- 로그인이 필요한 서비스에 접속 시도 시 바로 로그인 페이지로 리다이렉트
- 미가입회원도 바로 가입할 수 있도록 로그인 하단에 가입페이지로 이동 가능한 버튼 삽입
- 회원가입 및 로그인 시 잘못된 정보를 기입하면 알람창을 띄워 유저가 인식할 수 있도록 구성

3. 무VTI (선호장르조사)  
(이미지 삽입)
- 유저의 선호 장르를 조사하여 적절한 추천 알고리즘을 구축함과 동시에, 개인화 전략을 통해 서비스의 SNS 성격 강화

4. 메인페이지  
(로그인 후 메인페이지)
- 회원가입 및 로그인 시, 유저가 등록했던 무VTI를 기반으로 한 영화 추천 서비스 제공

5. 영화 세부 페이지  
(상세페이지이미지)
- 영화에 대한 간략한 정보와 함께, 리뷰 작성 기능 및 다른 유저들이 작성한 리뷰 목록 제공
- 좋아요 기능을 통한 간략한 선호도 표기

6. 리뷰 작성페이지
(이미지)
- 영화 상세페이지에서 즉시 해당 영화에 대한 리뷰 작성 가능
- 제목, 내용의 간결한 구성

7. 리뷰 상세페이지 
(이미지)
- 리뷰 내용과 함께 영화 제목 및 포스터, 작성자 정보 제공
- 리뷰작성자는 리뷰 수정, 삭제 가능
- 리뷰에 대한 댓글 작성 및 삭제 기능
- 리뷰가 마음에 들 경우, 작성자의 프로필 페이지로 즉시 이동할 수 있도록 구성

8. 유저프로필페이지(이미지)
- 해당 유저가 작성한 모든 리뷰 리스트 제공 및 열람 가능
- 접속 유저가 본인인지 타인인지에 따라 안내문구 다르게 출력
- 적극적인 교류를 위한 팔로우, 방명록 구현을 통해 SNS적 기능 강화
