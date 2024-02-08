from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def submit_form(request):
    if request.method == 'POST':
        # Handle form submission logic here
        # For example, you can access form data using request.POST
        form_data = request.POST
        # Process the form data as needed
        
        # Return an appropriate response
        return HttpResponse('Form submitted successfully!')
    else:
        return HttpResponse('Invalid request method!')
