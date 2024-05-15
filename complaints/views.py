from django.shortcuts import get_object_or_404, redirect, render

from complaints.forms import ComplaintForm
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


# ? create complaint
def create_complaint(request):
    form = ComplaintForm()
    if request.method == 'POST':
        form = ComplaintForm(data=request.POST)
        if request.user.is_superuser:
            form.add_error('', "Super users can't create complaints😔!")
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.created_by = request.user
            complaint.save()
            return redirect('complaint-list')
    return render(request, 'complaints/complaint-edit.html', {'form': form, 'btn_val': "Create Complaint"})

# ? edit complaint
def edit_complaint(request, pk: int | None = None):
    comp = get_object_or_404(Complaint, pk=pk)
    form = ComplaintForm(instance=comp)
    if request.method == 'POST':
        form = ComplaintForm(instance=comp, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaint-list')
    return render(request, 'complaints/complaint-edit.html', {'form': form, 'btn_val': "Update Complaint"})