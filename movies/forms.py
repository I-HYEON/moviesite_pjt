from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ('poster_url','user','like_users',)
        widgets = {
            'genre': forms.Select(choices=[('comedy','코미디'),('horror','공포'),('romance','로맨스'),('action','액션')]),
            'score': forms.NumberInput(attrs={'type':'number','step':0.5,'min':0,'max':5}),
            'release_date':forms.DateInput(attrs={'type':'date'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('movie','user',)