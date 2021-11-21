from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        age = request.POST["age"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if CustomUser.objects.filter(username=username).exists():
                return redirect("signup")
            
            user = CustomUser.objects.create_user(username=username, email=email, age=age, password=password)
            user.save()
            return redirect("login")
    
        return redirect("signup")

    return render(request, "registration/signup.html")

    # form = CustomUserCreationForm()
    # 
    # if request.method == "POST":
    #     form = CustomUserCreationForm(request.POST)

    #     if form.is_valid():
    #         user = CustomUser.objects.create_user(username=username, age=age, password=password)
    #         user.save()
    #         return redirect("login")

    # context = {
    #     "form": form
    # }

    # return render(request, "accounts/signup.html", context)

# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_rul = reverse_lazy("login")
#     template_name = "registration/signup.html"

