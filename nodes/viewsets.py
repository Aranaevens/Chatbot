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
        if node.node_id != 1:
            search = node.node_ancestry + '/' + str(node.node_id)
            # second_search = node.node_ancestry + '/' + str(node.node_id) + '/'
            children = Node.objects.filter(Q(node_ancestry=search))
            serializer = NodeSerializer(children, many=True)
            return Response(serializer.data)
        else:
            children = Node.objects.filter(Q(node_ancestry='1'))
            serializer = NodeSerializer(children, many=True)
            return Response(serializer.data)