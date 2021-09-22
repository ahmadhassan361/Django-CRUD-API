from functools import partial
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Products
from .serializers import ProductSeriliazer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST','PUT','DELETE'])
def handle_products(request):
    if request.method == 'GET':
        serial = request.GET.get('id', None);
        if serial is not None:
            product = Products.objects.get(id=serial)
            serializer = ProductSeriliazer(product)
            data = JSONRenderer().render(serializer.data)
            return HttpResponse(data,content_type='application/json')
        else:
            product = Products.objects.all()
            serializer = ProductSeriliazer(product,many=True)
            data = JSONRenderer().render(serializer.data)
            return HttpResponse(data,content_type='application/json') 
    if request.method == 'POST':
        serializer = ProductSeriliazer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'error':False,
                'message':'data save...'
            }
            return JsonResponse(res,safe=True)
        else:
            res = {
                'error':True,
                'message':serializer.errors
            }
            return JsonResponse(res,safe=True)

    if request.method == 'PUT':
        id = request.data.get('id')
        print(id)
        product = Products.objects.get(id=id)
        serializer = ProductSeriliazer(product,data= request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {
                'error':False,
                'message':'data updated...'
            }
            return JsonResponse(res,safe=True)
        else:
            res = {
                'error':True,
                'message':serializer.errors
            }
            return JsonResponse(res,safe=True)
    if request.method == 'DELETE':
        serial = request.data.get('id')
        product = Products.objects.get(id=serial)
        resp = product.delete()
        if resp is not None:
            res = {
                'error':False,
                'message':'record deleted...'
            }
            return JsonResponse(res,safe=True)
        else:
            res = {
                'error':True,
                'message':'something went wrong..'
            }
            return JsonResponse(res,safe=True)
