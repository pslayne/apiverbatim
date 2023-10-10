from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from .controllers import transcriber, firebase
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializer import MyTokenObtainPairSerializer

from . import models

storage_bucket = firebase.get_bucket()

@require_GET
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def transcribe(request):

    filename = request.GET.get('file_name')
    blob = storage_bucket.blob(f'audio/{filename}')
    blob.download_to_filename(f'audio/{filename}')
    transcription = transcriber.transcribe_batch(f'audio/{filename}')
    return JsonResponse({ 'message': transcription }, status = 200)

@require_POST
@csrf_exempt
def signup(request):
    user_name = request.POST.get('user_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    roles = request.POST.get('roles')

    if(user_name and email and password):
        try:
            exists = models.User.objects.get(email=email)
            if(exists):
                return JsonResponse({ 'message': "email already in use" } , status=403)
        except models.User.DoesNotExist:
            new_user = models.User.objects.create(
                username=user_name, 
                email=email
            )

            if roles:
                new_user.roles = roles
            
            new_user.set_password(password)
            new_user.save() 
            return JsonResponse({ 'message': 'created' }, status=201)
    else:
        return JsonResponse({ 'message': "one or more fields are blank or invalid" }, status=400)
    

@require_POST
@csrf_exempt
def login(request):

    email = request.POST.get('email')
    password = request.POST.get('password')

    if email and password:
        try:
            user = models.User.objects.get(email=email)
            if(user.check_password(password)):
                token = MyTokenObtainPairSerializer.get_token(user)
                return JsonResponse({ 
                    'user_name': user.username, 
                    'email': user.email,
                    'roles': user.roles.split(','),
                    'tokens': token
                    }, 
                    status=200)
            else:
                return JsonResponse({ 'message':'passwords don\'t match' }, status=400)
        except models.User.DoesNotExist:
            return JsonResponse({'message': 'user does not exists'}, status=404)
    else:
        return JsonResponse({ 'message': "one or more fields are blank or invalid" }, status=400)
        