customuser 모델을 만들고, 회원가입 crud 기능을 구현했다.

- 장고에서 제공하는 form을 사용해서 구현할 수 있었는데, 각 form마다 form을 만들때 요구하는 인자가 달라서 에러가 많이 났다.
Authentificationform 은 request를 인자로 요구하고,
PasswordChangeForm은 user를 넘겨줄때 'instance='를 안써주고 그냥 써도 된다.

- 회원가입 기능을 구현 시 forms 파일에 CustomUserCreationForm, CustomUserChangeForm을 만들때
class meta에는 meta를 상속해줄 것. 

- static 폴더에 따로 css 폴더를 만들어서 css 파일을 넣고 base.html과 연결해주려고 했는데, 경로설정을 잘못해서 적용이 안됐다.
경로 설정을 꼼꼼히 확인하기!