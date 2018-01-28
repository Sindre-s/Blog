from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
	posts = Post.objects.all()
	
	context = {
			'posts':posts
	}

	return render(request, 'blog/view_blogs.html', context)

@login_required
def create_blog(request):
	if(request.method =='POST'):
		print "request.POST", request.POST
		title = request.POST['title']
		author = request.POST['author']
		body = request.POST['body']
		u = User.objects.get(username=str(author))
		post = Post(title=title, author=u, text=body)
		post.save()

		return redirect('/post')
	else:
		users = User.objects.all()
		user = {
				'users':users
		}
		return render(request, 'blog/create_blog.html', user)

