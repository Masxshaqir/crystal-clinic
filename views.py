from django.shortcuts import render,redirect

from crystal import settings
from landing_page.models import Book ,Comment
from django.core.mail import send_mail
from django.contrib import messages
from django.db import transaction

# Create your views here.



def index(request):
    #get all comments from DB to list it in UI
    all_comments = list(Comment.objects.all().values('comment'))
    context = {'all_comments': all_comments}
    #check if request methos id POST or not
    if request.method == 'POST':
        try:
            #make this as transaction to excute it as abulk or rollback all
            with transaction.atomic():
                new_book  = Book(
                    name=request.POST.get('name', None),
                    email=request.POST.get('email', None),
                    phone=request.POST.get('phone', None),
                    date=request.POST.get('date', None),
                    time=request.POST.get('time', None)
                )
                new_book.clean()  # This will trigger validation
                new_book.save()

                message = f"""
                    Dear Crystal Client,
                    you have an appointment at {request.POST['date']} {request.POST['time']}

                    Thanks & BR
                """
                #send mail after reservation
                send_mail(
                    'Confirm Reservation',
                    message,
                    settings.EMAIL_HOST_USER,
                    [request.POST.get('email', None)],
                    fail_silently=False,
                )

                # Store success message in session
                request.session['success'] = 'You booked successfully at ' + str(request.POST['date']) + " " + str(request.POST['time'])

        except Exception as e:

            # Store error message in session
            request.session['error'] = str(e).replace('[','').replace(']','')

        return redirect(index)

    else:
        # Retrieve messages from session
        context['success'] = request.session.pop('success', None)
        context['error'] = request.session.pop('error', None)

        return render(request, 'index.html', context)

def add_comment(request):
    if request.method == 'POST':
        try :
            with transaction.atomic():

                new_comment = Comment.objects.create(comment = request.POST.get('comment',None))


                messages.add_message(request, messages.INFO, 'Comment Add successfully')
                return redirect('/#reviews')
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Error while submitting your comment')
            return redirect('/#reviews')
    else:
        return redirect('/#reviews')

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')