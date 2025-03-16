from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .helpers import error_response, generate_unique_short_code
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer
from django.db.utils import IntegrityError

@api_view(['POST'])
def create_short_url(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return error_response('Invalid Json!', status_code=status.HTTP_400_BAD_REQUEST)
    
    original_url = data.get('original_url')

    if not original_url:
        return error_response('Original URL is required', status_code=status.HTTP_400_BAD_REQUEST)
    
    existing_url = ShortURL.objects.filter(
        original_url=original_url
    ).first()
    
    if existing_url:
        return Response(ShortURLSerializer(existing_url).data, status=status.HTTP_200_OK)
    
    short_code = generate_unique_short_code()
    
    try:
        short_url = ShortURL.objects.create(
            original_url = original_url,
            short_code = short_code
        )
        
        serializer = ShortURLSerializer(short_url)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except IntegrityError:
        return error_response('Short URL creation failed. Try again!', status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrive_original_url_by_short_url(request, short_code):

    short_url = get_object_or_404(ShortURL, short_code=short_code)

    serializer = ShortURLSerializer(short_url)

    return Response(serializer.data, status=status.HTTP_200_OK)

def index(request):
    return render(request, 'index.html')