from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

ARTICLE_CATEGORY = (
    ("Siyaset-Yazı", "Siyaset-Yazı"),
    ("Siyaset-Haber", "Siyaset-Haber"),
    ("Spor-Yazı", "Spor-Yazı"),
    ("Spor-Haber", "Spor-Haber"),
    ("Müzik", "Müzik"),
    ("Sinema", "Sinema"),
    ("Edebiyat", "Edebiyat"),
    ("Sahne Sanatları", "Sahne Sanatları"),
    ("Görsel Sanatlar", "Görsel Sanatlar"),
    ("Gezi Notu", "Gezi Notu"),
    ("Çeviri", "Çeviri"),
)



class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE,verbose_name="Author")
    title = models.CharField(max_length= 50,verbose_name="Başlık")
    content = RichTextField(verbose_name = "İçerik")
    created_date = models.DateTimeField(auto_now_add= True,verbose_name="Creadet Date")
    article_image = models.FileField(blank=True,null=True,verbose_name="Makale Fotoğrafı")
    article_category = models.CharField(
        max_length=20,
        choices=ARTICLE_CATEGORY,
        default="Siyaset-Yazı",
        verbose_name="Makale Türü"
    )
    is_superarticle = models.BooleanField(verbose_name="Haftanın İçeriği Yap",default=0)
    def __str__(self):
     return self.title

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model): 
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="article" ,related_name="comments")
    comment_author = models.CharField(max_length= 50 ,verbose_name="c_author")
    comment_content = models.CharField(max_length=200,verbose_name="c_content")
    comment_date = models.DateTimeField(auto_now_add=True,verbose_name="comment_date")
    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']

class About(models.Model):
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE,verbose_name="Author",default=None)
    content = RichTextField(verbose_name = "İçerik")

