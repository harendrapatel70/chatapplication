from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ChatHistory(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "ChatHistory"
        verbose_name_plural = "ChatHistories"