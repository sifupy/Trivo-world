from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import  TextInput, EmailInput,DateField
from .models import *
class New_p(forms.ModelForm):
    class Meta:
        model=Post
        exclude=('author2','likes')
        widgets={
            'img':forms.ClearableFileInput(attrs={
                'class':"form-control my-form-field",
                'style': 'max-width: 500px;',
            }),
            'text':forms.Textarea(attrs={
                'class':"form-control my-form-field",
                'style': 'max-width: 500px;height:40px;max-height:120px;',
                'placeholder':"describe your trip",
            }),
            'location':forms.TextInput(attrs={
                'class':"form-control my-form-field",
                'style': 'max-width: 500px;',
                'placeholder':"where u traveled",
            }),
        }
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
        exclude=('Creatur','Total','Transport_costs','Food_costs','Other_costs')
        widgets={
            'Title':forms.TextInput(attrs={
                'class':"form-control my-form-field",
                'style': 'max-width: 500px;',
                'placeholder':"Title to ur trip",

            }),
            'Target':forms.TextInput(attrs={
                'class':"form-control my-form-field",
                'style': 'max-width: 500px;',
                'placeholder':"Where you will go",

            }),
            'date':forms.DateInput(format='%d/%m/%Y',attrs={
                'class':"form-control my-form-field",
                'style': 'max-width: 500px;',
                'placeholder':"date format : yyyy-mm-dd",
            }),
            'fin_date':forms.DateInput(format='%d/%m/%Y',attrs={
                'class':"form-control my-form-field",
                'style': 'max-width: 500px;',
                'placeholder':"date format : yyyy-mm-dd",
            }),
            'Descreption':forms.Textarea(attrs={
                'class':"form-control my-form-field",
                'style': 'max-width: 500px;height:100px;',
                'placeholder':"Some informations about the trip",

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
        exclude=('plan','num','n')
        #fields = ['name', 'email']
        widgets = {
            'morning': forms.Textarea(attrs={
                'class': "form-control my-form-field",
                'style': 'max-width: 300px;height:40px;max-height:120px;',
                'placeholder': 'what you will do in the morning'
                }),
            'middle_day':forms.Textarea(attrs={
                'class': "form-control my-form-field", 
                'style': 'max-width: 300px;height:40px;max-height:120px;',
                'placeholder': 'middle_day'
                }),
            'night': forms.Textarea(attrs={
                'class': "form-control my-form-field", 
                'style': 'max-width: 300px;height:40px;max-height:120px;',
                'placeholder': 'night'
                }),
            'description': TextInput(attrs={
                'class': "form-control my-form-field", 
                'style': 'max-width: 300px;',
                'placeholder': 'describe your day plan'
                }),
                
        }
class Location_search_form(forms.ModelForm):
    class Meta:
        model=Adress
        fields=['location']
        widgets={
            'location':forms.TextInput(attrs={
                'class':"",
                'style':"max-width:300px;",
                'placeholder':" Enter a location ",
            })
        }
        labels={
            'location':"",
        }