from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def book(request):
    return HttpResponse('这是jiangyetest')

def book_detail(request,book_id):
    text = '图书id是 %s'% book_id
    return HttpResponse(text)

def test(request):
    return HttpResponse('testjaingyebook')