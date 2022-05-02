from django.shortcuts import render

# Create your views here.
def contact_view(request):
    return render(request, 'contacts.html')


def contacts_form_view(request):
    return render(request, 'contacts-form.html')