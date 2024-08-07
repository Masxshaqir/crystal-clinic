from django.shortcuts import render, redirect

from crystal import settings
from landing_page.models import Book, Comment
from django.core.mail import send_mail
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout

# Create your views here.


import random
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
from .models import User


@login_required(login_url="/login/")
def add_appointment (request):
    if request.method == "POST":
        try:
            # make this as transaction to excute it as abulk or rollback all
            with transaction.atomic():
                new_book = Book(
                    name=request.POST.get("name", None),
                    email=request.POST.get("email", None),
                    phone=request.POST.get("phone", None),
                    date=request.POST.get("date", None),
                    time=request.POST.get("time", None),
                    user=request.user,
                )
                new_book.clean()  # This will trigger validation
                new_book.save()

                message = f"""
                    Dear Crystal Client,
                    you have an appointment at {request.POST['date']} {request.POST['time']}

                    Thanks & BR
                """
                # send mail after reservation
                send_mail(
                    "Confirm Reservation",
                    message,
                    settings.EMAIL_HOST_USER,
                    [request.POST.get("email", None)],
                    fail_silently=False,
                )

                # Store success message in session
                request.session["success"] = (
                    "You booked successfully at "
                    + str(request.POST["date"])
                    + " "
                    + str(request.POST["time"])
                )

        except Exception as e:

            # Store error message in session
            request.session["error"] = str(e).replace("[", "").replace("]", "")

        return redirect(index)


def index(request):
    # get all comments from DB to list it in UI
    all_comments = list(Comment.objects.all().values("comment"))
    all_Appointements=[]
    if request.user.is_authenticated:
        all_Appointements = list(
            Book.objects.filter(user=request.user, date__gte=datetime.now().date()).values(
                "id", "date", "time"
            )
        )
    context = {"all_comments": all_comments, "all_Appointements": all_Appointements}
        
    # check if request methos id POST or not
    # Retrieve messages from session
    context["success"] = request.session.pop("success", None)
    context["error"] = request.session.pop("error", None)

    return render(request, "index.html", context)






@login_required(login_url="/login/")
def add_comment(request):
    if request.method == "POST":
        try:
            with transaction.atomic():

                new_comment = Comment.objects.create(
                    comment=request.POST.get("comment", None)
                )

                messages.add_message(request, messages.INFO, "Comment Add successfully")
                return redirect("/#reviews")
        except Exception as e:
            messages.add_message(
                request, messages.ERROR, "Error while submitting your comment"
            )
            return redirect("/#reviews")
    else:
        return redirect("/#reviews")


@login_required(login_url="/login/")
def delete_book(request, ID):
    book = Book.objects.filter(id=ID)
    if book:
        book.delete()
        return redirect(index)
    else:
        messages.error("Book Not Found")
        return redirect(index)


@login_required(login_url="/login/")
def update_book(request):
    if request.method == "POST":
        try:
            book = Book.objects.get(id=request.POST.get("appointment-id", None))
            if book:
                book.date = request.POST.get("appointment-date", None)
                book.time = request.POST.get("appointment-time", None)
                book.clean()  # This will trigger validation
                book.save()
                request.session["success"] = "Book Updated Succefully"
                return redirect(index)
        except Exception as e:

            request.session["error"] = str(e).replace("[", "").replace("]", "")

        return redirect(index)
    else:
        return redirect(index)


def appointments(request):
    return render(request, "appointments.html")


def signup(request):
    try:
        if request.method == "POST":
            print(request.POST)
            if User.objects.filter(
                username=request.POST.get("username", None)
            ).exists():
                messages.error(request, "Username already exists")
                return render(request, "signup.html")

            if User.objects.filter(email=request.POST.get("email", None)).exists():
                messages.error(request, "Email already exists")
                return render(request, "signup.html")
            User.objects.create_user(
                username=request.POST.get("username", None),
                password=request.POST.get("password", None),
                email=request.POST.get("email", None),
            )
            return redirect(login)
        else:
            return render(request, "signup.html")

    except Exception as e:
        messages.error(request, str(e))
        return render(request, "signup.html")


def login(request):
    try:
        if request.method == "POST":
            user = authenticate(
                email=request.POST.get("email", None),
                password=request.POST.get("password", None),
            )
            if user is not None:
                auth.login(request, user)
                return redirect(index)
            else:
                return render(request, "login.html")
        else:
            return render(request, "login.html")

    except Exception as e:

        return render(request, "login.html")


@login_required(login_url="/login/")
def Logout(request):
    try:
        user = User.objects.filter(username=request.user.username)
        if user:
            logout(request)
            return redirect(index)

    except Exception as e:
        messages.error(request, str(e))
        return render(request, "login.html")
