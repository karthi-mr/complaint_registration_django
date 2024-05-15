from django.contrib.auth.models import User
from django.db import models

STATUS = [
    (1, 'Not Solved'),
    (2, 'In Progress'),
    (3, 'Solved'),
    (4, 'Closed'),
]

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self) -> str:
        return self.name

class Complaint(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    already_raised = models.BooleanField(default=False)
    old_ticket_id = models.CharField(max_length=250, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
