from django.shortcuts import render,redirect
from .models import Movie
from .forms import MovieForm, CommentForm

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request,'movies/index.html',context)

def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {'movie':movie,'comment_form':comment_form,}
    return render(request,'movies/detail.html',context)

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MovieForm(request.POST,request.FILES)
            if form.is_valid():
                movie = form.save()
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
    if form.is_valid():
    comment = form.save(commit=False)
    comment.movie = movie
    comment.save()
    #         return redirect('movies:detail',movie.pk)
    # else:
    #     form = CommentForm()
    # context = {'form':form,'movie':movie}
    return