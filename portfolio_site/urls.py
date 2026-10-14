from django.views.generic import TemplateView  # displays a template without a custom view
from django.shortcuts import render  # combines a template with data for the response
from django.urls import path  # connects web addresses to page views

def contact(request):
    # A submitted form arrives here as a POST request.
    if request.method == "POST":
        # Read the fields and remove spaces at the start and end.
        name = request.POST.get("name", "").strip()
        comment = request.POST.get("comment", "").strip()
        # Return the comment and name so the page can show a thank-you.
        if name and comment:
            return render(request, "contact.html", {"name": name, "comment": comment})
        # If either field is empty, show an error on the same page.
        return render(request, "contact.html", {"error": "Please add your name and a comment."})
    # A normal visit just displays the blank form.
    return render(request, "contact.html")

urlpatterns = [
    # Each path names a page; the name is used by Django's {% url %} links.
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("contact/", contact, name="contact"),
]
