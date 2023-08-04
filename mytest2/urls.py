"""mytest2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from mytestapp2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name='home'),
    path('addpost/', views.addpost, name = 'addpost'),
    path('article/edit/<int:pk>', views.updatepost, name = 'update'),
    path('article/<int:pk>', views.articlepage, name = 'article'),
    path('likes/<int:pk>', views.likespage, name = 'likes'),
    path('login/',views.loginpage, name= 'login'),
    path('article/<int:pk>/delete',views.deletepost, name= 'delete'),
    path('signup/',views.signup, name= 'signup'),
    path('logout/',views.logoutpage, name= 'logout'),
    path('profile/',views.profilepage, name= 'profile'),
    path('profileappear/',views.profileappear, name= 'profileappear'),
    path('contact/',views.contactpage, name= 'contact'),
    path('categories/<str:cats>',views.categoriespage, name= 'categories'),
    ]
