from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    post = {
        "title": "My First Blog Post",
        "description": "This is my first blog post. I am excited to share my thoughts and experiences with you.",
        "author": None,
        "date": datetime(2026, 1, 10, 10, 30),
        "comments_count": 5,
        "tags": ["django", "python", "web development"],
        "price": 100,
        "number":2,
    }
    return render(request, "blog/blog_details.html", {"post": post})