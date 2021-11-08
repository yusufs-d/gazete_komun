from django.db.models.query import RawQuerySet
from django.http import response
from django.shortcuts import redirect, render, HttpResponse,get_object_or_404
from django.urls import reverse
from .forms import ArticleForm, AboutForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import About, Article, Comment

# Create your views here.

def index(request):
    superarticles = Article.objects.filter(is_superarticle = 1)
    
    last_articles_query = Article.objects.all()
    last_articles = list()
    if len(last_articles_query)<6:
        for i in range(len(last_articles_query)):
            last_articles.append(last_articles_query[i])
    else:
        for i in range(6):
            last_articles.append(last_articles_query[i])

    return render(request,"index.html",{"s_articles":superarticles,"last_articles":last_articles})

def create_about(request):
    about = get_object_or_404(About)
    form = AboutForm(request.POST or None,instance=about)

    if form.is_valid():
        about_content = form.save(commit=False)
        about_content.author = request.user
        about_content.save()
        messages.success(request,"Hakkımızda Sayfası Başarıyla Güncellendi!")
        return redirect("dashboard")

    context = {
        "form" : form
    }
    return render(request,"create_about.html",context)

def about(request):
    abt = get_object_or_404(About,id=1)
    return render(request,"about.html",{"abt":abt})


def detail(request,id):
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()
    return render(request, "detail.html",{"article" : article, "comments" : comments})

@staff_member_required()
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }
    return render(request,"dashboard.html",context)

@staff_member_required()
def add_article(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    superarticles = Article.objects.filter(is_superarticle = 1)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        if len(superarticles)>=2 and article.is_superarticle:
            article.is_superarticle = 0
            article.save()
            messages.warning(request,"Makale Başarıyla Eklendi. Fakat En Fazla 2 Tane Haftanın İçeriği Olabileceği İçin Haftanın İçeriklerine Eklenemedi.")
            return redirect("dashboard")

        article.save()
        messages.success(request,"Makale Başarıyla Eklendi!")
        return redirect("dashboard")

    context = {
        "form" : form
    }
    return render(request,"add_article.html",context)

@staff_member_required()
def update_article(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None, request.FILES or None,instance=article)
    superarticles = Article.objects.filter(is_superarticle = 1)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        if len(superarticles)>=2 and article.is_superarticle:
            article.is_superarticle = 0
            article.save()
            messages.warning(request,"Makale Başarıyla Güncellendi. Fakat En Fazla 2 Tane Haftanın İçeriği Olabileceği İçin Haftanın İçeriklerine Eklenemedi.")
            return redirect("dashboard")

        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi!")
        return redirect("dashboard")

    context = {
        "form" : form
    }
    return render(request,"update.html",context)

@staff_member_required()
def delete_article(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi!")
    return redirect("dashboard")

@login_required(login_url="user:login")
def add_comment(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == "POST":
        comment_author = request.user
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author,comment_content = comment_content)
        newComment.article = article
        newComment.save()
        messages.success(request,"Yorum Başarıyla Eklendi!")
    return redirect(reverse("article:detail",kwargs={"id":id}))



def siyaset_yazi(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"siyaset-yazılar.html",{"articles" : articles})
    articles = Article.objects.filter(article_category = "Siyaset-Yazı")
    context = {
        "articles" : articles
    }
    return render(request,"siyaset-yazılar.html",context)

def siyaset_haber(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"siyaset-haberler.html",{"articles" : articles})
    articles = Article.objects.filter(article_category = "Siyaset-Haber")
    context = {
        "articles" : articles
    }
    return render(request,"siyaset-haberler.html",context)

def spor_yazi(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"spor-yazılar.html",{"articles" : articles})
    articles = Article.objects.filter(article_category = "Spor-Yazı")
    context = {
        "articles" : articles
    }
    return render(request,"spor-yazılar.html",context)

def spor_haber(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"spor-haberler.html",{"articles" : articles})
    articles = Article.objects.filter(article_category = "Spor-Haber")
    context = {
        "articles" : articles
    }
    return render(request,"spor-haberler.html",context)
def muzik(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"müzik.html",{"articles" : articles})
    articles = Article.objects.filter(article_category = "Müzik")
    context = {
        "articles" : articles
    }
    return render(request,"müzik.html",context)

def sinema(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"sinema.html",{"articles" : articles})
    articles = Article.objects.filter(article_category = "Sinema")
    context = {
        "articles" : articles
    }
    return render(request,"sinema.html",context)

def edebiyat(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"edebiyat.html",{"articles" : articles})
    articles = Article.objects.filter(article_category = "Edebiyat")
    context = {
        "articles" : articles
    }
    return render(request,"edebiyat.html",context)

def sahne(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"sahne_sanatları.html",{"articles" : articles})
    articles = Article.objects.filter(article_category = "Sahne Sanatları")
    context = {
        "articles" : articles
    }
    return render(request,"sahne_sanatları.html",context)

def gorsel(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"görsel_sanatlar.html",{"articles" : articles})
    articles = Article.objects.filter(article_category = "Görsel Sanatlar")
    context = {
        "articles" : articles
    }
    return render(request,"görsel_sanatlar.html",context)

def gezi(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"gezinotu.html",{"articles" : articles})
    articles = Article.objects.filter(article_category = "Gezi Notu")
    context = {
        "articles" : articles
    }
    return render(request,"gezinotu.html",context)

def ceviri(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"çeviri.html",{"articles" : articles})
    articles = Article.objects.filter(article_category = "Çeviri")
    context = {
        "articles" : articles
    }
    return render(request,"çeviri.html",context)