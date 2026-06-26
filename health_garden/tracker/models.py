#datas, sheets, models

from django.db import models
from datetime import date, datetime

class food(models.Model):
    date = models.DateField(default = date.today, help_text = "date of entry, must be the day of logging")
    name = models.CharField(max_length = 30, help_text = "Name of food", null=True)
    calories = models.PositiveIntegerField(help_text = "Calories of food")

    def __str__(self):
        return f"{self.date} – {self.name}({self.calories} kcal)"

#--------------------------------------------------------------------------------------------------------------------

class water(models.Model):
    date = models.DateField(default = date.today)
    time = models.TimeField(auto_now_add=True)
    name = models.CharField(max_length = 30, default = 'Water intake')
    amount = models.PositiveIntegerField(help_text="water drinked in mL")

    def __str(self):
        return f"{self.date}, {self.time} - {self.name}({self.amount} mL)"
    
#--------------------------------------------------------------------------------------------------------------------

class medication(models.Model):
    name = models.CharField(max_length=100)
    FREQUENCY_CHOICES = [
        ('daily', 'Every day'),
        ('weekly', 'Specific days'),
    ]
    frequency_type = models.CharField(max_length=10)
    DAYS_IN_WEEK = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ]
    days = models.CharField(blank=True)

    def __str__(self):
        if self.frequency_type == 'weekly':
            return f"{self.name} - weekly ({self.days})"
        else:
            return f"{self.name} - daily"
