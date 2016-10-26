"""word2vecmachine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

from django.contrib.auth.models import Word
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('word', 'vector')

# ViewSets define the view behavior.
class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'word', WordViewSet)
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'', include('word2vec.urls')),
    url(r'^rest-api/', include('rest_framework.urls')),
]
