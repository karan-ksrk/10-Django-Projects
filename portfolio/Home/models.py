from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    year = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    year = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

class Design(models.Model):
    name = models.CharField(max_length=50, null=True)
    level = models.IntegerField(help_text="%")

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50, null=True)
    level = models.IntegerField(help_text="%")

    def __str__(self):
        return self.name

class CodingSkill(models.Model):
    name = models.CharField(max_length=50, null=True)
    level = models.IntegerField(help_text="%")
    
    def __str__(self):
        return self.name

class Knowlegde(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Interest(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100, null=True)
    desciption = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Resume(models.Model):
    FREELANCE = (
        ('Avalibale', 'Available'),
        ('Note Available', 'Not Available'),
    )
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    residence = models.CharField(max_length=50, null=True)
    freelance = models.CharField(max_length=50, null=True, choices=FREELANCE) 
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    services  = models.ManyToManyField(Service, null=True)
    experience  = models.ManyToManyField(Experience, null=True)
    education  = models.ManyToManyField(Education, null=True)
    design  = models.ManyToManyField(Design, null=True)
    language  = models.ManyToManyField(Language, null=True)
    coding_skill  = models.ManyToManyField(CodingSkill, null=True)
    knowlegde  = models.ManyToManyField(Knowlegde, null=True)
    interest = models.ManyToManyField(Interest, null=True)
    team = models.ManyToManyField(Team, null=True)
    future_goals = models.TextField(max_length=1000, null=True)
    

    def __str__(self):
        return self.name
    

