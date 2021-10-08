from django.urls import path
from .views import home ,edit ,test

urlpatterns = [path("", home, name="home"),
               path("test/new/", test, name="test"),
               path("<str:pk>/",edit ,name = 'edit')]
# path('edit/<str:pk>/', edit ,name = "edit"),
# path('apply/<str:pk>/', apply, name="apply"),
# path('values/', values, name="home"),
# path('ex/', example_view, name="home"),

#
