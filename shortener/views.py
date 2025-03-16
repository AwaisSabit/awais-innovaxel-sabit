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

@api_view(['GET', 'PUT', 'DELETE'])
def retrive_update_delete_url(request, short_code):

    short_url = get_object_or_404(ShortURL, short_code=short_code)

    if request.method == 'GET':
        serializer = ShortURLSerializer(short_url)

        short_url.access_count += 1
        short_url.save(update_fields=['access_count'])

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        new_url = request.data.get('original_url')

        if not new_url:
            return error_response('New URL is required', status=status.HTTP_400_BAD_REQUEST)

        existing_url = ShortURL.objects.filter(original_url=new_url).exclude(short_code=short_code).first()
        if existing_url:
            return Response({
                "error": "This original URL is already associated with another short code.",
                "existing_short_code": existing_url.short_code
            }, status=status.HTTP_400_BAD_REQUEST)

        short_url.original_url = new_url
        short_url.save()

        serializer = ShortURLSerializer(short_url)
        
        return Response({
            "message": "Short URL updated successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        short_url = get_object_or_404(ShortURL, short_code=short_code)

        short_url.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_url_statistics(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)

    return Response({
        "id": short_url.id,
        "url": short_url.original_url,
        "shortCode": short_url.short_code,
        "createdAt": short_url.created_at,
        "updatedAt": short_url.updated_at,
        "accessCount": short_url.access_count
    }, status=status.HTTP_200_OK)
