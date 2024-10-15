from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import ollama

@csrf_exempt
def predict(request):
    pass

def teste(request):
    client = ollama.Client(host='http://localhost:11434')
    response = client.chat(model='tinydolphin', messages=[
      {
        'role': 'user',
        'content': 'Why is the sky blue?',
      },
    ])
    return HttpResponse(response)
