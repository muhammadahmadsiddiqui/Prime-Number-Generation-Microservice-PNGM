import time
import psutil
from concurrent.futures import ThreadPoolExecutor
from django.http import JsonResponse

executor = ThreadPoolExecutor(max_workers=1)
prime_numbers = []

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def generate_prime_numbers(from_num, to_num):
    global prime_numbers
    prime_numbers = [num for num in range(from_num, to_num + 1) if is_prime(num)]

def generate(request):
    from_num = int(request.GET.get('from', '1'))
    to_num = int(request.GET.get('to', '100'))
    executor.submit(generate_prime_numbers, from_num, to_num)
    return JsonResponse({'status': 'Prime number generation started'})

def monitor(request):
    k = int(request.GET.get('k', '1'))
    cpu_percent = psutil.cpu_percent(interval=k)
    memory_percent = psutil.virtual_memory().percent
    return JsonResponse({'cpu_percent': cpu_percent, 'memory_percent': memory_percent})

def get(request):
    global prime_numbers
    return JsonResponse({'prime_numbers': prime_numbers})
