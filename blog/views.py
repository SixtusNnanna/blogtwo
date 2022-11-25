from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment, Reply, Profile
from django.views.generic import ListView, DetailView,CreateView,UpdateView, DeleteView
from.forms import EditpostForm, PostForm, CommentForm, ReplyForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    Liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        Liked = False
    else:
        post.likes.add(request.user)
        Liked = True
    return HttpResponseRedirect(reverse('blog:article-detail', args = [str(pk)]))
    
class HomeView(ListView):
    models = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.order_by('-published')


    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context 

    
        
def CategoryList(request):
    categorylist = Category.objects.all()
    return render(request, 'cate_list.html', {'categorylist': categorylist})
        
class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.get_total_like()
        Liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            Liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["Liked"] = Liked
        return context 


class AddPostView(CreateView):
    model = Post
    template_name = 'the_post.html'
    #fields = ['title', 'body']
    form_class = PostForm

class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    #fields = '__all__'
    form_class = CommentForm
    success_url = reverse_lazy('blog:home')
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class AddReplyView(CreateView):
    model = Reply
    template_name = 'add_reply.html'
    #fields = '__all__'
    form_class = ReplyForm
    success_url = reverse_lazy('blog:home')

    
    def form_valid(self, form):
        form.instance.comment_id = self.kwargs['pk']
        return super().form_valid(form)


def CategoryPost(request, cats):
    
    category_post = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'category.html', {
        'cats':cats.title().replace('-', ' '), 'category_post':category_post})


class AddCategoryView(CreateView):
    model = Category
    template_name = 'cate.html'
    fields = '__all__'
    #form_class = PostForm


class UpdatePostView(UpdateView):
    model = Post 
    template_name = 'update_post.html'
    #fields = ['title', 'body']
    form_class = EditpostForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog:home')
