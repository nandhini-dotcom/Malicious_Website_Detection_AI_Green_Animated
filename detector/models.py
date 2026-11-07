from django.db import models
from django.contrib.auth.models import User
class URLPrediction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    url=models.URLField(max_length=2000)
    prediction=models.CharField(max_length=20)
    confidence=models.FloatField(default=0)
    risk_level=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.prediction} - {self.url}"
