from django.db import models

# Create your models here.

class Tutor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    subjects_taught = models.CharField(max_length=50)
    students_enrolled = models.IntegerField(default=0)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

class SubjectsTaught(models.Model):
    parent_person = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    subject_text = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_text



class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    subjects_struggling = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

class SubjectsStruggling(models.Model):
    parent_person = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    subject_text = models.CharField(max_length=50)
    current_grade = models.CharField(max_length=2)

    def __str__(self):
        return self.subject_text