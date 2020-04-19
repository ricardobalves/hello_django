from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade, soma1, soma2):
    soma = soma1+soma2
    return HttpResponse('<h1>Hello {} de {} anos e soma é {}</h1>'.format(nome, idade, soma))