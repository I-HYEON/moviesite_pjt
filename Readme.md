customuser 모델을 만들고, 회원가입 crud 기능을 구현했다.

- 장고에서 제공하는 form을 사용해서 구현할 수 있었는데, 각 form마다 form을 만들때 요구하는 인자가 달라서 에러가 많이 났다.
Authentificationform 은 request를 인자로 요구하고,
PasswordChangeForm은 user를 넘겨줄때 'instance='를 안써주고 그냥 써도 된다.

- 회원가입 기능을 구현 시 forms 파일에 CustomUserCreationForm, CustomUserChangeForm을 만들때
class meta에는 meta를 상속해줄 것. 

- static 폴더에 따로 css 폴더를 만들어서 css 파일을 넣고 base.html과 연결해주려고 했는데, 경로설정을 잘못해서 적용이 안됐다.
경로 설정을 꼼꼼히 확인하기!


2023.4.16
1. 영화를 추천하는 페이지와 리뷰를 작성하는 페이지를 따로 분리.
2. TMDB API를 사용하여 현재 상영중인 영화를 보여주는 index(), 영화 상세정보를 보여주는 get_detail() 구현.

- index()함수는 api를 사용하여 현재 상영중인 영화 정보를 가져와 데이터를 처리하고, 이걸 context에 저장한 다음, index.html 템플릿에 전달해 보여준다.
- get_detail() 함수는 사용자가 클릭한 특정 영화의 id를 기반으로 해당 영화의 상세정보를 가져와서 이걸 movie_info 딕셔너리에 저장하고, get_detail 템플릿에 전달하여 사용자에게 보여준다.