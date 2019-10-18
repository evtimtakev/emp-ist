from django.db import models


# Defines client model
class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "{0}".format(self.name)


# Defines employee model wit relation to project
class Employee(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)

    def __str__(self):
        return "{0}".format(self.name)


# Defines project model with relation to client
class Project(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)
    employees = models.ManyToManyField(Employee, related_name='employee')

    def __str__(self):
        return "{0}".format(self.title)

