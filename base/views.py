from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Book
from .serializers import BookSerializer
@api_view(["GET","POST"])

def home_to_all_books(request):
    books = Book.objects.all()
    seriazlizer = BookSerializer(books, many=True)
    return Response(seriazlizer.data)

@api_view(["POST"])
def add_book(request):
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(["GET","PUT", "DELETE"])
def single_book(request, id):
    try:
        a_book = Book.objects.get(pk=id)
        
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        a_book.delete()
        return Response({"message":f"Book {id} deleted"},status=status.HTTP_200_OK)
        
    serializer = BookSerializer(a_book)
    return Response(serializer.data)