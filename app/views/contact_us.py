from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import render
from django.conf import settings




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
        msg.send()

        clientmail(name,email)
        
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
        msg.send()

        
        
    except Exception as e:
        print("Error sending email:", e)
        raise Exception("Problem sending email")


from django.shortcuts import redirect
from django.urls import reverse
def contact_us(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        subject=request.POST['subject']
        message=request.POST['message']
        mail(name,email,contact,subject,message)
        return redirect(reverse("home"))  # Redirect to the URL named 'new_view_name'
    else:
        return render(request,"home/contact_us.html")