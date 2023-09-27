from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from .controllers import transcriber
from . import models

@require_GET
def transcribe(request):
    # receber um arquivo de áudio
    transcription = transcriber.transcribe_batch('./audio/woman1_wb.wav')
    return JsonResponse({ 'message': transcription }, status = 200)

@require_POST
@csrf_exempt
def signup(request):
    user_name = request.POST['user_name']
    email = request.POST['email']
    #criptografar
    password = request.POST['password']

    if(user_name and email and password):
        try:
            exists = models.User.objects.get(email=email)
            if(exists):
                return JsonResponse({ 'message': "email already in use" } , status=403)
        except models.User.DoesNotExist:
            new_user = models.User.objects.create(name=user_name, email=email,password=password)
            new_user.save() 
            return JsonResponse({ 'message': 'created' }, status=201)
    else:
        return JsonResponse({ 'message': "one or more fields are blank or invalid" }, status=400)