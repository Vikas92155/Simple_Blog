from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Comment, Post


class IndexView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'latest_post_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Post.objects.order_by('-pub_date')[:5]

def addcomment(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	try:
		add_comment = post.comment_set.create(comment_text = request.POST['comment'])
	except (KeyError, Comment.DoesNotExist):
		return render(request, 'blog/detail.html', {
			'post': post,
			'error_message': "You didn't add any comment.",
		})
	return HttpResponseRedirect(reverse('blog:index'))
