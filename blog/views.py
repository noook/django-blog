from django.shortcuts import render, redirect
from django import forms
from django.views import generic
from .models import Article, ArticleForm


class IndexView(generic.ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = "latest_articles"

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.all().order_by("-published_date")


class ArticleView(generic.DetailView):
    model = Article
    template_name = "blog/article.html"


class ArticleCreate(generic.CreateView):
    model = Article
    fields = ["title", "content"]


def create(request):
    if request.method == "GET":
        form = ArticleForm()
        data = {"form": form}
        return render(request, "create.html", data)
    else:
        form = ArticleForm(request.POST)
        if form.is_valid:
            print(form)
            form.save()
            return redirect("index")

