from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from post.models import Stream, Post, Tag, Likes, PostFileContent
from post.forms import NewPostForm
from stories.models import Story, StoryStream

from comment.models import Comment
from comment.forms import CommentForm


from django.contrib.auth.decorators import login_required

from django.urls import reverse
from authy.models import Profile


# Create your views here.
@login_required
def mainindex(request):
	user = request.user
	posts = Post.objects.all()
	
	# group_ids = []
	for post in posts:
		post_items = Post.objects.all()
		
		
	post_items = Post.objects.all().order_by('-posted')	

	template = loader.get_template('uquery/main_index.html')

	context = {
		'post_items': post_items,		
	}

	return HttpResponse(template.render(context, request))


@login_required
def index(request):
	user = request.user
	posts = Stream.objects.filter(user=user)

	paginator = Paginator(posts, 15)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	stories = StoryStream.objects.filter(user=user)


	group_ids = []

	for post in posts:
		group_ids.append(post.post_id)
		
	post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')		

	template = loader.get_template('uquery/index.html')

	context = {
		'post_items': post_items,
		'stories': stories,
		'page_obj': page_obj,

	}

	return HttpResponse(template.render(context, request))

def PostDetails(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	user = request.user
	profile = Profile.objects.get(user=user)
	favorited = False

	#comment
	comments = Comment.objects.filter(post=post).order_by('-date')
	
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=user)
		#For the color of the favorite button

		if profile.favorites.filter(id=post_id).exists():
			favorited = True

	#Comments Form
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.user = user
			comment.save()
			return HttpResponseRedirect(reverse('postdetails', args=[post_id]))
	else:
		form = CommentForm()


	template = loader.get_template('uquery/post_detail.html')

	context = {
		'post':post,
		'favorited':favorited,
		'profile':profile,
		'form':form,
		'comments':comments,
	}

	return HttpResponse(template.render(context, request))


@login_required
def NewPost(request):
	user = request.user
	tags_objs = []
	files_objs = []

	if request.method == 'POST':
		form = NewPostForm(request.POST, request.FILES)
		if form.is_valid():
			files = request.FILES.getlist('content')
			caption = form.cleaned_data.get('caption')
			tags_form = form.cleaned_data.get('tags')

			tags_list = list(tags_form.split(','))

			for tag in tags_list:
				t, created = Tag.objects.get_or_create(title=tag)
				tags_objs.append(t)

			for file in files:
				file_instance = PostFileContent(file=file, user=user)
				file_instance.save()
				files_objs.append(file_instance)

			p, created = Post.objects.get_or_create(caption=caption, user=user)
			p.tags.set(tags_objs)
			p.content.set(files_objs)
			p.save()
			return redirect('index')
	else:
		form = NewPostForm()

	context = {
		'form':form,
	}

	return render(request, 'uquery/newpost.html', context)

def tags(request, tag_slug):
	tag = get_object_or_404(Tag, slug=tag_slug)
	posts = Post.objects.filter(tags=tag).order_by('-posted')

	template = loader.get_template('uquery/tag.html')

	context = {
		'posts':posts,
		'tag':tag,
	}

	return HttpResponse(template.render(context, request))



@login_required
def like(request, post_id):
	user = request.user
	post = Post.objects.get(id=post_id)
	current_likes = post.likes
	liked = Likes.objects.filter(user=user, post=post).count()

	if not liked:
		like = Likes.objects.create(user=user, post=post)
		#like.save()
		current_likes = current_likes + 1

	else:
		Likes.objects.filter(user=user, post=post).delete()
		current_likes = current_likes - 1

	post.likes = current_likes
	post.save()

	return HttpResponseRedirect(reverse('postdetails', args=[post_id]))

@login_required
def favorite(request, post_id):
	user = request.user
	post = Post.objects.get(id=post_id)
	profile = Profile.objects.get(user=user)

	if profile.favorites.filter(id=post_id).exists():
		profile.favorites.remove(post)

	else:
		profile.favorites.add(post)

	return HttpResponseRedirect(reverse('postdetails', args=[post_id]))


def about_us(request):

	template = loader.get_template('uquery/about.html')

	context = {
		
	}

	return HttpResponse(template.render(context, request))

	
def report_bug(request):

	template = loader.get_template('uquery/report_bug.html')

	context = {
		
	}

	return HttpResponse(template.render(context, request))


def news_forum(request):

	template = loader.get_template('uquery/news.html')

	context = {
		
	}

	return HttpResponse(template.render(context, request))

def setting(request):

	template = loader.get_template('uquery/setting.html')

	context = {
		
	}

	return HttpResponse(template.render(context, request))

def apps(request):

	template = loader.get_template('uquery/apps.html')

	context = {
		
	}

	return HttpResponse(template.render(context, request))

def trend(request):

	template = loader.get_template('uquery/trend.html')

	context = {
		
	}

	return HttpResponse(template.render(context, request))

def helpme(request):

	template = loader.get_template('uquery/help.html')

	context = {
		
	}

	return HttpResponse(template.render(context, request))

def shop(request):

	template = loader.get_template('uquery/shop.html')

	context = {
		
	}

	return HttpResponse(template.render(context, request))


