from django.db import models


# GENDER_CHOICES = (
#      ("M", "male"),
#      ("F", "female"),
#      ("O", "others"),
# )
# BOOL_CHOICES = (
#     ("Y", 'Yes'), 
#     ("N", 'No'),
# )
# OPTION_CHOICES = (
#     ("Y", "YES"),
#     ("N", "NO"),
#     ("D", "Don't know"),
# )
# OPTION1_CHOICES = (
#     ("Y", "YES"),
#     ("N", "NO"),
#     ("M", "Not that much"),
# )
# OPTION2_CHOICES = (
#     ("A", "it happens all the time"),
#     ("B", "it happens too often, but not all the time"),
#     ("C", "it happens sometimes"),
#     ("D", "it never happens"),
# )
class Questionaries(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=1)
    school = models.CharField(max_length=100,default="")
    ques_five = models.CharField(max_length=1)
    ques_six = models.TextField(max_length=200,default="")
    ques_seven = models.CharField(max_length=1)
    ques_eight = models.CharField(max_length=1)
    ques_nine = models.CharField(max_length=200,default="")
    ques_ten = models.CharField(max_length=1)
    ques_eleven = models.CharField(max_length=1)
    description = models.TextField(max_length=200,default="")
    ques_twelve = models.CharField(max_length=200,default="")
    ques_thirteen = models.CharField(max_length=200)
    ques_fourteen = models.CharField(max_length=200,default="")


    def __str__(self):
        return self.name

    