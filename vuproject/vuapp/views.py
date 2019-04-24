# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Books
from .serializers import BooksSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


def index(request):
    context = {
        'days': [1, 2, 3],
    }
    return render(request, 'index.html',context)

@csrf_exempt
def main_page(request):
    return render(request, 'main.html')




class BooksViewSet(APIView):
    def get(self,request):
        book_id =request.GET.get('id')
        if book_id:
            queryset = Books.objects.filter(pk=book_id)
        else:
            queryset = Books.objects.all()
        serializer= BooksSerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        title = request.data.get('title')
        author = request.data.get('author')
        price = request.data.get('price')
        edition = request.data.get('edition')
        Books.objects.create(title=title,author=author,price=price,edition=edition)
        return Response('Saved Successfully')
    def put(self,request):
        title = request.data.get('title')
        author = request.data.get('author')
        price = request.data.get('price')
        edition = request.data.get('edition')
        update_books = Books.objects.filter(pk = request.data.get('id'))
        update_books.update(title=title,author=author,price=price,edition=edition)
        return Response('Updated Successfully')

    def delete(self,request):
        book_id =request.GET.get('id')
        Books.objects.filter(pk=book_id).delete()
        return Response('Deleted Successfully')
