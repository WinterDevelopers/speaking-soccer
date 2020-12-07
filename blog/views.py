from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import generic
from django.urls import reverse
from blog.models import Post, Comment
from blog.forms import CommentForm
from blog.subscription import SubscribersForm


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'blog/index.html'
    paginate_by = 8
    context_object_name = 'post_list'
 


class EplPost(generic.ListView):
    context_object_name = 'epl'
    queryset = Post.objects.filter(category = 0).order_by('-created_on')
    template_name = 'blog/epl.html'
    paginate_by = 10

class SeriaAPost(generic.ListView):
    context_object_name = 'seriaA'
    queryset = Post.objects.filter(category = 2).order_by('-created_on')
    template_name = 'blog/seriaa.html'
    paginate_by = 10

class BundesligaPost(generic.ListView):
    context_object_name = 'bundesliga'
    queryset = Post.objects.filter(category = 3).order_by('-created_on')
    template_name = 'blog/bundesliga.html'
    paginate_by = 10


class LaligaPost(generic.ListView):
    context_object_name = 'laliga'
    queryset = Post.objects.filter(category = 1).order_by('-created_on')
    template_name = 'blog/laliga.html'
    paginate_by = 10


class League1Post(generic.ListView):
    context_object_name = 'league1'
    queryset = Post.objects.filter(category = 4).order_by('-created_on')
    template_name = 'blog/league1.html'
    paginate_by = 10

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

def post_detail(request, slug):
    template_name = 'blog/detail.html'
    post = get_object_or_404(Post, slug=slug)
    others = Post.objects.filter(category = 0).order_by('-created_on')
    comments = post.comments.filter(active=True)
    new_comment = None
    post.counts = post.counts + 1
    post.save()
  


    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)

            new_comment.post = post
            
            new_comment.save()
        
    else:
        comment_form = CommentForm()
        
    return render(request, template_name, {'post': post, 'others':others,
                                                'comments': comments, 
                                                'new_comment': new_comment,
                                                'comment_form':comment_form })
    
  

class DemoForm(generic.FormView):
    template_name = 'detail.html'
    form_class = CommentForm
    success_url = '/post_detail/'


def sub_view(request):
    sub = SubscribersForm()

    if request.method == 'POST':
        sub = SubscribersForm(request.POST)

        if sub.is_valid():
            sub.save(commit=True)
            return HttpResponse('<p><b>welcome</b></p>')
    
    else:
        sub = SubscribersForm
        
    return render(request, 'blog/subscription.html', {'sub':sub})

