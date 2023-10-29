from django import forms
from .models import *
class New_p(forms.ModelForm):
    class Meta:
        model=Post
        exclude=('author2','likes')
# creating a form
class InputForm(forms.Form):

    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)

class CantactForm(forms.Form):
    email=forms.EmailField()
    subject=forms.CharField(max_length=40,required=False)
    message=forms.TimeField()
class New_com(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=('author','post_id')

        
class New_profile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=('user',)
class New_plan(forms.ModelForm):
    class Meta:
        model=Plan
        exclude=('Creatur','Total')
class Join_request_form(forms.ModelForm):
    class Meta:
        model=Plan_member3
        exclude=('member','plan','badge','status')
class Accept_request_form(forms.ModelForm):
    class Meta:
        model=Plan_member3
        exclude=('member','plan','status')