import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from main.forms import RegistrationForm
from main.models import Candidates
import logging

from main.serializers import CandidatesSerializer

logger = logging.getLogger('django')


def index(request):
    return render(request, 'main/index.html', {})


class Registration(CreateView):
    model = Candidates
    form_class = RegistrationForm
    template_name = 'main/registration.html'
    success_url = '/'

    def form_valid(self, form):
        return super(Registration, self).form_valid(form)


class CandidatesViewSet(viewsets.ModelViewSet):
    serializer_class = CandidatesSerializer
    queryset= Candidates.objects.all()
    admin_x=False
    def list(self, request, pk=None,*args, **kwargs):
        candidates = Candidates.objects.all().order_by('-created_at')
        self.admin_x = request.META['HTTP_X_ADMIN']
        if self.validate_admin():
            return Response(candidates.data, status=status.HTTP_200_OK)
        else:
            return Response("UNAUTHORIZED", status=status.HTTP_401_UNAUTHORIZED)

    def validate_admin(self):
        if self.admin_x == "1" :
            return True
        else:
            return False

    def retrieve(self, request, *args, **kwargs):
        self.admin_x = request.META['HTTP_X_ADMIN']
        resume=self.get_object().resume
        filename = resume.file.name.split('/')[-1]
        response = HttpResponse(resume.file, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response