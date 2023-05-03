from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Notes(BaseModel):
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.body[:50]

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"