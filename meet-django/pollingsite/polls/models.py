from django.db import models

# Create your models(classes) here.
class Poll(models.Model):
	question = models.CharField(max_length=100)

class Answer(models.Model):
	ans_text = models.CharField(max_length=50)
	votes = models.IntegerField(default=0)
	poll = models.ForeignKey(Poll)


