from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .serializers import (
    ProdutoSerializer,
    LoteSerializer
)
from .models import (
    Lote,
    Produto
)
# Create your views here.

class LoteList(ListCreateAPIView):
    queryset = Lote.objects.all().order_by('nome_produto')
    serializer_class = LoteSerializer

class LoteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Lote.objects.all().order_by('nome_produto')
    serializer_class = LoteSerializer


class ProdutoList(ListCreateAPIView):
    queryset = Produto.objects.all().order_by('nome')
    serializer_class = ProdutoSerializer


class ProdutoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all().order_by('nome')
    serializer_class = ProdutoSerializer