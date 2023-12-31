"""
URL configuration for wedbln project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from weddad.views import *
from django.contrib.auth.views import LoginView ,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',first,name="home"),
    path('signup/',sign,name="signup"),
    path('addpost',newp,name="addpostyy"),
    path('login',LoginView.as_view(template_name='auth_login.html'),name="login"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('profile/<user_id>',profilepage,name="profile"),
    path('post_update/<post_id>',updatedef,name="pst-update"),
    path('post_p/<post_id>',postpagedef,name="post_page"),
    path('map',my_map,name="mapping"),
    path('settings/my_account',my_accountdef,name="my_account"),
    path('plans/',planview,name="plans"),
    path('plans/plan/<memberchip_id>',plview,name="spec_plan"),
    path('Plans/join_request/<mypk>',jrview,name="Join_request_page"),
    path('like/<int:pk>',Likeview,name='like_page'),
    path('cantacts',cantactview,name='cantacts'),
    path('Posts/delete<post_id>',Delete_post_view,name="delete_post"),
    path('plans/trip_planner/<plan_id>',trip_planner,name="tripplanner"),
    path('plans/delete/<plan_id>',Delete_plan_view,name="delete_plan"),

  
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)