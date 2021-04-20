from django.http import JsonResponse
# Create your views here.
def index(request):
    data = {
        "message": "Welcome to Solzbank App"
    }
    return JsonResponse(data)