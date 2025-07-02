from django.contrib.auth.models import User
from django.db import models

class Subscription(models.Model):
    subscriber = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE)
    subscribed_to = models.ForeignKey(User, related_name='subscribers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('subscriber', 'subscribed_to')  # чтобы не было дублей

    def __str__(self):
        return f"{self.subscriber} подписан на {self.subscribed_to}"