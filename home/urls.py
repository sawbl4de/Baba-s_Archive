from django.contrib import admin
from django.urls import path
from home import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('writings/', views.poems, name='writings'),
    path('writings/poems', views.poems, name='poems'),
    path('writings/articles', views.articles, name='articles'),
    path('writings/stories', views.stories, name='stories'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
