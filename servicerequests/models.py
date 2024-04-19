from django.db import models
import os

def attachment_upload_path(instance, filename):
    # Get the filename and extension
    filename, ext = os.path.splitext(filename)
    # Return the upload path
    return f'servicerequests/attachments/{instance.id}{ext}'

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to=attachment_upload_path, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

def attachment_upload_path(instance, filename):
    # Get the filename and extension
    base_filename, ext = os.path.splitext(filename)
    # Construct the upload path based on the instance's ID
    return f'servicerequests/{instance.id}/{base_filename}{ext}'
