from django.db import models
import uuid

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    recipe = models.TextField(default="")
    image_url = models.URLField()
    slug = models.SlugField()
    price = models.FloatField(default=0.0)
    is_private = models.BooleanField()

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()