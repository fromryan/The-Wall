from django.urls import path
from . import views

urlpatterns = [
	path('',views.index),
	path('register', views.register),
	path('login_process', views.login_process),
	path('wall', views.wall),
	path('logout', views.logout),
	path('post_ing', views.post_ing),
	# path('comment_ing', views.comment_ing),
	path('delete/<int:id>', views.delete),
]