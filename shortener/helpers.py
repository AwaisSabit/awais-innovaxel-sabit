import random
import string
from rest_framework.response import Response
from rest_framework import status


def generate_unique_short_code():
    
    from shortener.models import ShortURL
    
    length = 6
    chars = string.digits + string.ascii_letters

    while True:
        short_code = ''.join(random.choices(chars, k=length))
        if not ShortURL.objects.filter(short_code=short_code).exists():
            return short_code
        

def error_response(message, status_code):
    return Response({'error': message}, status=status_code)