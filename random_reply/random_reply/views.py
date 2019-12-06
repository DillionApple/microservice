import random

from django.http import HttpResponse

def api_random_reply(request):

    length = request.GET.get("length", 1024)

    s = [chr(random.randint(ord('a'), ord('z'))) for _ in range(length)]

    return HttpResponse(s)