from django.db import models

# class Language(models.Model):
#     name = models.CharField(max_length=50)
#     # paradigm = models.CharField(max_length=50)
#     image =  models.ImageField(upload_to='obrazy', null=True, blank=True)

#     def __str__(self):
#         return self.name

################################################################################
class Task(models.Model):
    #id = models.AutoField(primary_key=True)
    configJSONFile = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

class ObjFile(models.Model):
    objFile = models.FileField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)




