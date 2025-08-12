from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    website_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.subject.name})"

class Availability(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    time_slot = models.CharField(max_length=100)  

    def __str__(self):
        return f"{self.teacher.name} - {self.time_slot}"
