from django.shortcuts import get_object_or_404, redirect, render

from complaints.forms import ComplaintEditForm, ComplaintForm
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

# ? view complaint detail
def view_complaint(request, pk: int | None = None):
    try:
        comp = Complaint.objects.get(pk=pk)
    except Complaint.DoesNotExist:
        return render(request, 'complaints/complaint-detail.html', {'no_complaint': True})
    return render(request, 'complaints/complaint-detail.html', {'complaint': comp, 'no_compaint': False})


# ? edit complaint
def edit_complaint(request, pk: int | None = None):
    comp: Complaint = get_object_or_404(Complaint, pk=pk)
    form = ComplaintEditForm(instance=comp)
    if request.method == 'POST':
        form = ComplaintEditForm(instance=comp, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            if data.get("already_raised"):
                old_ticket: int | None = data.get("old_ticket_id")
                try:
                    Complaint.objects.get(id=old_ticket)
                    form.save()
                except Complaint.DoesNotExist:
                    form.add_error('old_ticket_id', f"Ticket with above id not found");
                    return render(request, 'complaints/complaint-edit.html', {'form': form, 'btn_val': "Update Complaint"})
            form.save()
            return redirect('view-complaint', comp.id) # type: ignore
    return render(request, 'complaints/complaint-edit.html', {'form': form, 'btn_val': "Update Complaint"})