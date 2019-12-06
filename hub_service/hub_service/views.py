import requests

from django.http import HttpResponse

from hub_service.config import REQUEST_URLS


def api_hub(request):

    for url in REQUEST_URLS:
        response = requests.get(url)
        print(response.text)

    return HttpResponse("Success")