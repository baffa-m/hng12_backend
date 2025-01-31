from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
# Create your views here.
@api_view(['GET'])
def info(request):
    return Response({
        "email": "ahmadalmustapha4@gmail.com",
        "current_datetime": datetime.now().replace(microsecond=0).isoformat()+"Z",
        "github_url": "https://github.com/baffa-m/hng12_backend"
    })
