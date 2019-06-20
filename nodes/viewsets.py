from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from django.db.models import Q
from .models import Node
from .serializers import NodeSerializer


class NodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    @detail_route()
    def get_children(self, request, pk=None):
        node = self.get_object()
        first_search = node.node_ancestry + '/' + node.node_id
        second_search = node.node_ancestry + '/' + node.node_id + '/'
        children = Node.objects.filter(Q(Node=first_search) | Q(Node__startswith=second_search))
        serializer = NodeSerializer(children)
        return Response(serializer.data)