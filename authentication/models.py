from django.db import models

class CustomUser(models.Model):
    ROLES = (
        ('student', 'Student'),
        ('technician', 'Technician'),
        ('admin','admin')
    )

    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return self.username
class CustomItem(models.Model):
    LAB=(
        ("LBB-011","LBB-011"),
        ("LBB-015","LBB-015"),
        ("LBB-016","LBB-016"),
    )
    ITEMS=(
        ("projector","projector"),
        ("keyboard","keyboard"),
        ("mouse","mouse"),
        ("monitor","monitor"),
        ("system unit","system unit"),
        ("printer","printer"),
        ("networking toolkits","networking toolkit"),
        ("extension cable","extension cable"),
    )
    CONDITION=(
        ("Working","Working"),
        ("Faulty","Faulty"),
        ("Damaged","Damaged"),
    )
    item_name=models.CharField(max_length=50,choices=ITEMS)
    serial_number=models.CharField(max_length=50)
    condition=models.CharField(max_length=50,choices=CONDITION)
    lab=models.CharField(max_length=50,choices=LAB)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.item_name
    