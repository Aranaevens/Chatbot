from rest_framework import routers
from nodes.viewsets import NodeViewSet

router = routers.DefaultRouter()

router.register(r'node', NodeViewSet)