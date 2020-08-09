from django.db import models

class Ans(models.Model):
	req=models.TextField()

	def __str__(self):
		return self.req
