from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.hello, name='hello'),
	url(r'^hello2/', views.hello2),
	url(r'^similarity/', views.Similarity.as_view()),
]
