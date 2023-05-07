from rest_framework import routers, viewsets

from .models import Word
from .serializers import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
