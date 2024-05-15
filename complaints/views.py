from django.shortcuts import render

from complaints.models import Complaint


# ? dashboard view
def dashboard(request):
    return render(request, 'complaints/dashboard.html')

# ? complaints list view
def complaints_list(request):
    if request.user.is_superuser:
        complaints = Complaint.objects.all().order_by('-created')
    else:
        complaints = Complaint.objects.filter(created_by=request.user).order_by('-created')
    return render(request, 'complaints/complaint-list.html', {'complaints': complaints})