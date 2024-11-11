from django.shortcuts import render, HttpResponse, get_object_or_404, reverse, redirect
from django.contrib import messages
from .models import BirthdayWish, CustomerUser
from django.template.loader import render_to_string
from .forms import EditWishEvent

from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from datetime import datetime

# View to handle the form submission for saving user details
def birthday_view(request):
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        user = request.user
        if user.is_authenticated:
            # Extract the form data
            name = request.POST['name']
            birth_date = request.POST['date']
            email = request.POST['email']
            
            # Create a new CustomerUser object and save the form data
            customer_user = CustomerUser(user=user, name=name, birth_day=birth_date, email=email)
            customer_user.save()
        
            # Display a success message
            messages.success(request, "Thank you! Your friend's details have been saved, and they will receive a birthday wish on their special day.")
            # Render the index page after successful form submission
            return render(request, 'my_app/index.html', {"message": "There was some problem submitting the form"})
    
        # If the form was not submitted correctly, show an error message
        else:
            messages.error(request, 'Please fill all the details')
            # Render the index page with an error message
            return render(request, 'my_app/index.html', {"message": "There was some problem submitting the form"})
    return render(request, "my_app/index.html", {})



def birthday_archive(request):
    wishes = CustomerUser.objects.filter(user=request.user)
    context = {'wishes': wishes}
    print(wishes)
    return render(request, 'my_app/wish_list.html', context=context)
    
    
    
def delete_wishevent(request, pk):
    entry = get_object_or_404(CustomerUser, pk=pk, user= request.user)
    entry.delete()
    messages.success(request, "This is birthday even has been deleted")
    return redirect('wish-list')



def edit_wishevent(request):
    customer_user = get_object_or_404(CustomerUser, user=request.user)
    if request.method == "POST":
        form = EditWishEvent(request.POST, instance=customer_user)
        if form.is_valid():
            form.save()
            return redirect("wish-list")
    else:
        form = EditWishEvent(instance = customer_user)
    
    return render(request, 'my_app/edit_wish_event.html', {'form': form})
        
        
        
# Function to send birthday wishes to users whose birthday is today
def send_birthday_wish():
    # Get the current date
    today = datetime.now().date()
    
    # Query to get users whose birthday matches today's date (month and day)
    birthdays = CustomerUser.objects.filter(birth_day__month=today.month, birth_day__day=today.day)
    print("Above Line ran successfully!")  # Print to confirm the query executed
    
    # Iterate over all the users whose birthday is today
    for wish in birthdays:
        # Define the email subject
        subject = "Happy Birthday from Team!"
        
        # Calculate the user's age based on their birth year and today's year
        age = today.year - wish.birth_day.year
        print(age)  # Print to confirm the age calculation
        
        message = f""  # You can customize the message here if needed
        
        # Prepare the HTML content for the birthday email
        html_message = render_to_string("my_app/birthday.html",
                                        {
                                            'name': wish.name,
                                            'age': age,
                                            'message': message
                                        })
        
        # Send the email using Django's send_mail function
        send_mail(subject,
                  message,
                  'akshatraj2607@gmail.com',  # Sender's email
                  [wish.email],  # Recipient's email (user's email)
                  fail_silently=False,
                  html_message=html_message)  # Send the email in HTML format
        
        print("Mail sent successfully!")  # Print confirmation of email sent
        
        # Save a record in the BirthdayWish model for future reference
        confirmation = BirthdayWish(name=wish.name, message=message)
        confirmation.save()


# Function to schedule the birthday wish sending process
def send_wish():
    # Create a background scheduler to run tasks in the background
    scheduler = BackgroundScheduler()
    
    # Schedule the send_birthday_wish function to run daily at 18:10
    scheduler.add_job(send_birthday_wish, 'cron', hour=16, minute=32)
    
    # Start the scheduler
    scheduler.start()




            