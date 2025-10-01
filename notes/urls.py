from django.urls import path,include
from .views import NoteViewSet
# from django.urls import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path("api/", include(router.urls)), 
]

#api/notes/, GET request
#api/notes/ POST request
# api/notes/1 UPDATE request
# api/notes/1 DELETE request
# api/notes/1