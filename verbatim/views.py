from django.shortcuts import render
from django.http import HttpResponse
from . import transcriber

def transcribe(request):
    transcription = transcriber.transcribe_batch('./audio/woman1_wb.wav')
    return HttpResponse(transcription)