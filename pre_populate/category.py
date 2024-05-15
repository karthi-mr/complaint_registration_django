from complaints.models import Category

Category.objects.bulk_create([
    Category(name="Harassment"),
    Category(name="Bullying "),
    Category(name="Discrimination"),
    Category(name="Working Conditions"),
    Category(name="Communication"),
    Category(name="Pay and benefits grievances"),
    Category(name="Employee benefits"),
    Category(name="Unfair Pay"),
    Category(name="Retaliation"),
    Category(name="Workload grievances"),
    Category(name="Favoritism"),
    Category(name="Incompetent Managers"),
    Category(name="Lack of Recognition"),
    Category(name="Micromanagement"),
    Category(name="workload"),
])