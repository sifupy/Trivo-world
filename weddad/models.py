from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    img = models.ImageField(upload_to="media",null=True)
    text=models.TextField()
    published_time=models.DateTimeField(auto_now_add=True,null=True)
    author2=models.ForeignKey(User,related_name='userposts',on_delete=models.CASCADE)
    location=models.CharField()
    likes=models.ManyToManyField(User,related_name='trip_post')
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.text
class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField(max_length=150,null=True)
    profile_pic=models.ImageField(upload_to="profile_pics",null=True)
    def __str__(self):
        return str(self.user)
    
    
class Comment(models.Model):
    author=models.ForeignKey(User,related_name='usercomments',on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    text=models.TextField()
    published_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.post_id.text + " " + self.author.username
class Plan(models.Model):
    Creatur=models.ForeignKey(User,related_name='userplans',on_delete=models.CASCADE)
    Title=models.CharField(max_length=80)
    Target=models.CharField(max_length=80)
    Descreption=models.TextField(null=True,blank=True)
    date=models.DateField()
    Transport_costs=models.IntegerField(null=True)
    Food_costs=models.IntegerField(null=True)
    Other_costs=models.IntegerField(null=True)
    Total=models.IntegerField(null=True,blank=True)
    def save(self, *args, **kwargs):
        self.Total = self.Transport_costs +self.Food_costs + self.Other_costs
        super(Plan, self).save(*args, **kwargs)
    def __str__(self):
        return self.Creatur.username + " " + self.Title
class Plan_member3(models.Model):
    member=models.ForeignKey(User,related_name='Plan_memberchip',on_delete=models.CASCADE)
    plan=models.ForeignKey(Plan,related_name='members',on_delete=models.CASCADE)
    badge=models.CharField(max_length=25,null=True,blank=True)
    status=models.CharField(blank=True,default="Non")
    def __str__(self):
        return self.member.username +" "+ self.plan.Title

    