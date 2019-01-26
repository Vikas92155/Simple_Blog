from django.db import models


class Post(models.Model):
	post_text = models.CharField(max_length=1000)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.post_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=200)
	def __str__(self):
		return self.comment_text