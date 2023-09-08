from django.contrib import admin
from django.urls import path
from home import views
from django.urls import include
from django.contrib.auth import views as auth_views




urlpatterns = [
	path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('writings/', views.poems, name='writings'),
    path('writings/poems', views.poems, name='poems'),
    path('writings/articles', views.articles, name='articles'),
    path('writings/stories', views.stories, name='stories'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
    
