from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from langchain.llms import CTransformers
import json

# LLM 모델 초기화
llm = CTransformers(model="llama-2-7b-chat.ggmlv3.q2_K.bin", model_type="llama")

@api_view(['POST'])
def chat(request):
    message = request.data.get('message')
    response = handle_message(message)
    return Response({'response': response})

def home(request):
    return render(request, 'home.html')

def handle_message(message):
    return "안녕하세요!"

def translate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        source_text = data.get('text', '')
        if source_text:
            # LLM을 사용하여 번역 실행
            translation = llm.predict("translate Korean to German: " + source_text)
            # JSON 형태로 번역 결과 반환
            return JsonResponse({'translated_text': translation})
        else:
            # 텍스트가 제공되지 않았을 경우 에러 메시지 반환
            return JsonResponse({'error': 'No text provided for translation.'})
    else:
        # POST 요청이 아닌 경우 에러 메시지 반환
        return JsonResponse({'error': 'Invalid request method'})