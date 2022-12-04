import os

from django.http import HttpResponse, FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from app_theory.models import Theory
from django.template import Context, Template


class Test(APIView):

    def get(self, request):
        return Response({
            'message': 'ahihi',
            'type': 2
        }, status=200)

    def post(self, request):
        a = request.data['username']
        b = request.data.get('ldskjsdks')
        # b = request.data['ldskjsdks']
        return Response({
            'message': 'Post successfully = )))',
            'type': 1
        })


class GetTheory(APIView):
    def get(self, request):
        template_name = request.GET.get('template')
        theory = Theory.objects.filter(name=template_name)
        if theory.count() == 0:
            return Response({
                'message': f'Dont have any template name {template_name}!',
                'type': 2
            }, status=200)
        return HttpResponse(theory[0].content.replace('\n', ''))


class ReturnNoneImage(APIView):
    def get(self, request):
        img_url = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/images/1x1.png')
        img = open(img_url, 'rb')
        response = FileResponse(img)
        return response
