from django.urls import include, path
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter

from questions.api import views as qv

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewSet)


urlpatterns = [
    path("", include(router.urls)),

    path("questions/<slug:slug>/answer/",
        qv.AnswerCreateAPIView.as_view(), name='answer-create'),
    
    path("questions/<slug:slug>/answers/",
        qv.AnswerListAPIView.as_view(), name='answer-list'),
    
    path("answers/<int:pk>/",
        qv.AnswerRUDApiView.as_view(), name='answer-detail'),
    
    path("answers/<int:pk>/like/",
        qv.AnswerLikeAPIView.as_view(), name='answer-like')


]
