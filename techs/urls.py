from django.urls import path
from . import views

urlpatterns = [
    path("techs", views.techViewCreate.as_view()),
    path("techs", views.techViewList.as_view()),
    path("techs/<int:pk>/", views.techViewPatchDelete.as_view()),
]
