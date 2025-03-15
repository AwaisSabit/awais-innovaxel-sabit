import random
import string

def generate_unique_short_code():
    
    from shortener.models import ShortURL
    
    length = 6
    chars = string.digits + string.ascii_letters

    while True:
        short_code = ''.join(random.choices(chars, k=length))
        if not ShortURL.objects.filter(short_code=short_code).exists():
            return short_code