from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Article, Comment
from datetime import datetime

def articles(request):
    context = {}

    articles = Article.objects.all()

    context["articles"] = articles

    return render(request, "articles/article_list.html", context)

def article_create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            article = Article.objects.create(
                title=request.POST["title"],
                body=request.POST["body"],
                author=request.user
            )
            return redirect("article_details", article.id)
        
        return render(request, "articles/article_create.html")
    
    return redirect("login")

def article_details(request, pk):
    context = {}

    article = Article.objects.get(id=pk)

    context["article"] = article

    if request.method == "POST":
        comment = Comment.objects.create(
            article=article,
            author=request.POST["name"],
            comment=request.POST["comment"]
        )

    return render(request, "articles/article_details.html", context)

def article_edit(request, pk):
    context = {}

    article = Article.objects.get(id=pk)

    if request.user.is_authenticated:
        if request.user == article.author or request.user.is_staff:
            if request.method == "POST":
                article.title = request.POST["title"]
                article.body = request.POST["body"]
                article.date = datetime.now()
                article.save()
                return redirect("article_details", article.id)

            context["article"] = article

            return render(request, "articles/article_edit.html", context)

        return redirect("article_details", article.id)

    return redirect("login")

def article_delete(request, pk):
    article = Article.objects.get(id=pk)

    if request.user.is_authenticated:
        if request.user == article.author or request.user.is_staff:
            if request.method == "POST":
                article.delete()
                return redirect("articles")

            return render(request, "articles/article_delete.html")

        return redirect("article_details", article.id)

    return redirect("login")

def comment_delete(request, pk):    
    comment = Comment.objects.get(id=pk)

    if request.user == comment.article.author or request.user.is_staff:
        comment.delete()
        
    return redirect("article_details", comment.article.id)

# class ArticleListView(ListView):
#     model = Article
#     template_name = "articles/article_list.html"

# class ArticleDetailView(LoginRequiredMixin, DetailView):
#     model = Article
#     template_name = "articles/article_details.html"

# class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Article
#     template_name = "articles/article_edit.html"
# 
#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

# class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Article
#     template_name = "articles/article_delete.html"
#     success_url = reverse_lazy("articles")
# 
#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

# class ArticleCreateView(LoginRequiredMixin, CreateView):
#     model = Article
#     template_name = "articles/article_create.html"
#     fields = [
#         "title",
#         "body"
#     ]
# 
#   def form_valid(self, form):
#       form.instance.author = self.request.user
#       return super().form_valid(form) 
