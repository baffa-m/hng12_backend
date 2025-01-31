from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timezone
# Create your views here.
@api_view()
def info(request):
    return Response({
        "email": "ahmadalmustapha4@gmail.com",
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/baffa-m"
    })