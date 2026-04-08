from django.db import models


class Suggestion(models.Model):
    name = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Suggestion from {self.name or 'Anonymous'} ({self.created_at:%Y-%m-%d})"
