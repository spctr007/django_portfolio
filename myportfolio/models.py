from django.db import models


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)
    email_address = models.EmailField()
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=11)
    degree = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.employee)


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=3)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.employee)


class Testimonial(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    testimonial = models.CharField(max_length=500)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return "{} for {}".format(self.name, self.employee)
