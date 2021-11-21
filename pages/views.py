from django.shortcuts import render

def home_page(request):
    return render(request, "home.html")

# class HomePageView(TemplateView):
#     template_name = "home.html"
