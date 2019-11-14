from django.conf.urls import url
from rest_framework import routers

from main.views import CandidatesViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'candidates', CandidatesViewSet)
router.register(r'/get', CandidatesViewSet)
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^register$', views.Registration.as_view(), name='registration'),

]
