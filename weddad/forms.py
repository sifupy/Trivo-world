from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import  TextInput, EmailInput,DateField
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
    message=forms.CharField()
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
        widgets={
            'date':forms.DateInput(format='%d/%m/%Y',attrs={
                'class':"my-form-field",
                'placeholder':"date format: dd-mm-yyyy"
            }),
        }
class Join_request_form(forms.ModelForm):
    class Meta:
        model=Plan_member3
        exclude=('member','plan','badge','status')
class Accept_request_form(forms.ModelForm):
    class Meta:
        model=Plan_member3
        exclude=('member','plan','status')
class Day_planner_form(forms.ModelForm):
    class Meta:
        model=Day_Planner
        exclude=('plan','num')
        #fields = ['name', 'email']
        widgets = {
            'morning': TextInput(attrs={
                'class': "form-control my-form-field",
                'style': 'max-width: 300px;',
                'placeholder': 'what you will do in the morning'
                }),
            'middle_day': TextInput(attrs={
                'class': "form-control my-form-field", 
                'style': 'max-width: 300px;height:150px',
                'placeholder': 'middle_day'
                }),
            'night': TextInput(attrs={
                'class': "form-control my-form-field", 
                'style': 'max-width: 300px;',
                'placeholder': 'night'
                }),
            'description': TextInput(attrs={
                'class': "form-control my-form-field", 
                'style': 'max-width: 300px;',
                'placeholder': 'describe your day plan'
                }),
                
        }