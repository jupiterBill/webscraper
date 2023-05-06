from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length= 500)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.search
    def recent_search(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1) and self.timestamp<= timezone.now()
    class Meta:
        verbose_name_plural = 'Searches'
