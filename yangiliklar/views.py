from django.shortcuts import render
from .models import News, Category

# Create your views here.

def index(request):
    return render(request, "index.html")

def news_view(request):
  news = Category.object.all()
  
  context = {"news":news}
  
  return render(request, "news.html", context=context)

