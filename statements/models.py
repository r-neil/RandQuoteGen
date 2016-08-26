from django.db import models

# Create your models here.
class Statement(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	quote = models.TextField()
	author = models.CharField(max_length=100)
	already_used = models.BooleanField(default=False)

	def __str__(self):
		return '{}: {}'.format(self.quote, self.author)