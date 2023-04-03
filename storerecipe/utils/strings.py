import string
from django.utils.crypto import get_random_string

def generate_random_url():
    """generate random url"""
    _url = get_random_string(20, string.ascii_letters)
    return _url