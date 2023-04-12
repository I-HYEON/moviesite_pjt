from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model

# Create your views here.

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm(request)

    context = {'form':form}
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('movies:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user) 
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm() 
    context = {'form':form}
    return render(request,'accounts/signup.html',context)


def delete(request):
    request.user.delete() 
    auth_logout(request) 
    return redirect('movies:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save() 
            return redirect('movies:index') 
    else:
        form = CustomUserChangeForm(instance=request.user) 
    context = {'form':form}
    return render(request,'accounts/update.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()  
            update_session_auth_hash(request,form.user)
            return redirect('movies:index')  
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request,'accounts/change_password.html',context)

def profile(request,username):
    '''
    url로 접근을 하면, 프로필 페이지를 렌더해주는 기능
    그냥 models.py에서 User로 가져오지 않는 이유가 뭐지?
    '''
    User = get_user_model()  # get_user_model을 사용하면 현재 user 테이블을 가져오는건가?
    person = User.objects.get(username=username)  # 특정 user 인스턴스를 넘겨주는것?
    context = {
        'person':person,
    }
    return render(request,'accounts/profile.html',context)


def follow(request,user_pk):
    '''
    user_pk로 들어온 user를 찾아서 팔로우한다는건가? user_pk로들어온user가 다른 user를 팔로우한다는건가?
    전자임~~
    '''
    if request.user.is_authenticated:
        person = get_user_model().objects.get(pk=user_pk)  # 특정 user 인스턴스를 콕찝어 person에 할당한다
        if person != request.user:  # 현재 요청한 유저와 지금 팔로하려는 유저가 다른 경우에만
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        
        return redirect('accounts:profile')
    return redirect('accounts:login')