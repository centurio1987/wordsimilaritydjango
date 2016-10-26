from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.http.response import HttpResponse
from rest_framework import routers, serializers, viewsets
import json
from . import word2vec_proxy


# Create your views here.
@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def hello(request):
	generator = schemas.SchemaGenerator(title='Bookings API')
	return response.Response(generator.get_schema(request=request))

def hello2(request):
	result = word2vec_proxy.Word2vecInstance.getSimilarity(positive=['hello'])
	result_dict = {}
	for word, vector in result:
		result_dict[word] = vector
	return HttpResponse(json.dumps(result_dict))

class Similarity(GenericAPIView):
	def get(self, request, *args, **kwargs):
		positive = request.query_params.getlist('positive[]')
		negative = request.query_params.getlist('negative[]')

		if negative.count(''):
			result = word2vec_proxy.Word2vecInstance.getSimilarity(positive=positive)
		else:
			result = word2vec_proxy.Word2vecInstance.getSimilarity(positive=positive, negative=negative)

		result_dict = {}
		for word, vector in result:
			result_dict[word] = vector
		return response.Response(result_dict)
		#return HttpResponse(request.query_params.get('word'))
'''
	def post(self, request, *args, **kwargs):
		positive = [];
		negative = [];
		positive = request.data['positive']
		negative = request.data['negative']
		result = word2vec_proxy.Word2vecInstance.getSimilarity(positive=positive, negative=negative)
		result_dict = {}
		for word, vector in result:
			result_dict[word] = vector
		return response.Response(result_dict)
'''
