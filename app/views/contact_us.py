from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages

from django.shortcuts import redirect
from django.urls import reverse
from app.models import ContactMessage



def mail(name,email,contact,subject,message):
    try:
        from_email = settings.EMAIL_HOST_USER
        
        # Correct template_path and render the HTML template with the provided data
        template_path = 'mail_templates/company.html'
        context = {
            'name': name,
            'contact': contact,
            'message':message,
            'email':email,
        }
        
        # Render the HTML template to a string
        message = render_to_string(template_path, context)
        
        to = "anupmandal828109@gmail.com"
        
        # Create an email message object and attach the HTML message
        msg = EmailMultiAlternatives(subject, '', from_email, [to])
        msg.attach_alternative(message, 'text/html')
        try:
            msg.send()
            clientmail(name,email)
        except Exception as e:
            print("Error sending email:", e)
            raise Exception("Problem sending email check password")
        
    except Exception as e:
        print("Error sending email:", e)
        raise Exception("Problem sending email")


def clientmail(name,email):
    try:
        from_email = settings.EMAIL_HOST_USER
        subject = "ABCD pvt.LTD"
        # Correct template_path and render the HTML template with the provided data
        template_path = 'mail_templates/client.html'
        context = {
            'name': name,
        }
        
        # Render the HTML template to a string
        message = render_to_string(template_path, context)
        
        to = email
        
        # Create an email message object and attach the HTML message
        msg = EmailMultiAlternatives(subject, '', from_email, [to])
        msg.attach_alternative(message, 'text/html')


        try:
            msg.send()
        except Exception as e:
            print("Error sending email:", e)
            raise Exception("Problem sending email check password")

        
        
    except Exception as e:
        print("Error sending email:", e)
        raise Exception("Problem sending email")


def contact_us(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['contact']
        subject=request.POST['subject']
        message=request.POST['message']
        
        if not (name and email and phone and subject and message):
            messages.error(request, "All fields are required.")
            return render(request, "home/contact_us.html")

        try:
            # Save the contact message to the database
            ContactMessage.objects.create(fullname=name, email=email, phone=phone, subject=subject, message=message)

            # Send emails
            mail(name, email, phone, subject, message)

            messages.success(request, "Your message has been sent successfully.")
            return redirect(contact_us)  # Redirect to the home page
        except Exception as e:
            # Handle any errors that occur during email sending
            messages.error(request, "There was a problem sending your message. Please try again later.")
            return render(request, "home/contact_us.html")
    else:
        return render(request, "home/contact_us.html")
