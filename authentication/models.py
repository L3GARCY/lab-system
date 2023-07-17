from django.db import models


class CustomUser(models.Model):
    ROLES = (
        ('student', 'Student'),
        ('technician', 'Technician'),
        ('admin', 'admin')
    )

    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return self.username


class CustomItem(models.Model):
    LAB = (
        ("lbb-011", "LBB-011"),
        ("lbb-015", "LBB-015"),
        ("lbb-016", "LBB-016"),
    )
    ITEMS = (
        ("projector", "Projector"),
        ("keyboard", "Keyboard"),
        ("mouse", "Mouse"),
        ("monitor", "Monitor"),
        ("system-unit", "System-unit"),
        ("printer", "Printer"),
        ("toolkit", "Toolkit"),
        ("extension cable", "Extension cable"),
    )
    CONDITION = (
        ("working", "Working"),
        ("faulty", "Faulty"),
        ("damaged", "Damaged"),
    )
    item_name = models.CharField(max_length=50, choices=ITEMS)
    serial_number = models.CharField(max_length=50)
    condition = models.CharField(max_length=50, choices=CONDITION)
    lab = models.CharField(max_length=50, choices=LAB)

    def __str__(self):
        return self.item_name
class CustomBorrow(models.Model):
    pass