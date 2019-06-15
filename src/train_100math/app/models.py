from django.db import models


# Create your models here.
class Score(models.Model):
    class Meta:
        ordering = ['-created']

    created = models.DateTimeField(auto_now=True)
    q_count = models.PositiveIntegerField(verbose_name='問題数')
    sucess_count = models.PositiveIntegerField(verbose_name='正解数')
    score = models.PositiveIntegerField(verbose_name='点数')
