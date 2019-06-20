from django.db import models

class Node(models.Model):
    node_id = models.AutoField(primary_key=True)
    node_ancestry = models.CharField(max_length=100)
    node_text = models.TextField()
    