from django.shortcuts import render,redirect
from .models import Movie, Comment, Tag
from .forms import MovieForm, CommentForm
import requests

# Create your views here.
api_key = 'a3d6989298145a295df2fb4735b1535c'
base_url = 'https://api.themoviedb.org/3'

def index(request):
    url = f'{base_url}/movie/now_playing?api_key={api_key}&language=ko-KO&page=1'
    response = requests.get(url)
    data = response.json()['results']

    movies = []
    for movie in data:
        dict = {}
        dict['title'] = movie['title']
        dict['release_date'] = movie['release_date']
        dict['overview'] = movie['overview']
        dict['poster_path'] = f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}"
        dict['movie_id'] = movie['id']
        movies.append(dict)
    context = {'movies':movies}
    return render(request,'movies/index.html',context)

def get_detail(request,movie_id):
    url = f'{base_url}/movie/{movie_id}?api_key={api_key}&language=ko-KO'
    response = requests.get(url)
    data = response.json()

    movie_info = {}
    movie_info['title'] = data['title']
    movie_info['genres'] = data['genres']
    movie_info['overview'] = data['overview']
    movie_info['poster_path'] = f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    movie_info['release_date'] = data['release_date']
    movie_info['runtime'] = data['runtime']

    context = {'movie_info':movie_info}
    
    return render(request,'movies/get_detail.html',context)

def review(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request,'movies/review.html',context)

def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    comments = movie.comments.all()
    comment_form = CommentForm()
    context = {'movie':movie,'comment_form':comment_form,'comments':comments}
    return render(request,'movies/detail.html',context)

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MovieForm(request.POST,request.FILES)
            if form.is_valid():
                movie = form.save(commit=False)
                movie.user = request.user
                movie.save()

                # 태그 추가 부분
                # 현재 태그가 인풋박스로 나타나지 않아 해결 필요
                tag_names = request.POST.get('tags', '').split(',')
                for tag_name in tag_names:
                    tag_name = tag_name.strip()
                    if not tag_name:
                        continue
                    tag, _ = Tag.objects.get_or_create(name=tag_name)
                    movie.tags.add(tag)

                return redirect('movies:detail',movie.pk)
        else:
            form = MovieForm()

        context = {'form':form}
        return render(request,'movies/create.html',context)
    else:
        return redirect('accounts:login')
        
    
def update(request,pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail',movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {'form':form,'movie':movie}
    return render(request,'movies/update.html',context)

def delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')


def comments_create(request,post_pk):
    movie = Movie.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()

    return redirect('movies:detail',movie.pk)

'''
특정post의 특정 comment를 삭제해야함
어케함,,?
comment를 특정해서 지우고, 해당 post 페이지를 그대로 리다이렉트
'''
def comments_delete(request,post_pk,comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    comment.delete()
    return redirect('movies:detail',post_pk)

def likes(request,post_pk):
    '''
    만약에 log인한사용자라면 일반적인로직으로 빠질건데, 그건또다시 두가지로 나눔
      만약에 해당 게시글의 likes 레코드들 중 현 user이 존재하면, 좋아요취소
      만약에 else면 좋아요를 추가하게끔 한다
    '''
    
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=post_pk)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        return redirect('movies:index')
    return redirect('accounts:login')