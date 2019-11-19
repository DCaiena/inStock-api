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

    """
    sobescrevendo o método POST para adicionar lógica de quantidade de produto
    no lote
    """
    def post(self, request, *args, **kwargs):
        produto = request.data
        lote = Lote.objects.get(pk=int(produto['lote']))
        if lote.quantidade is not None:
            lote.quantidade += 1
        else:
            lote.quantidade = 1
        lote.save()
        return self.create(request, *args, **kwargs)


class ProdutoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all().order_by('nome')
    serializer_class = ProdutoSerializer

    def delete(self, request, *args, **kwargs):
        produto = kwargs.get('pk')
        produto = Produto.objects.get(pk=produto)
        lote = produto.lote
        lote.quantidade -= 1
        lote.save()
        return self.destroy(request, *args, **kwargs)

