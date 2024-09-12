from django.db import models

# Create your models here.
class Album(models.Model):
    """This album class will be used to create album objects.

        :Attribute int id: Album ID
        :Attribute str title: Album title
        :Attribute date release_date: Album release date 
        :Attribute str label: Record label 
        :Attribute str description: Album description
    
        :Method: __str__ method"""
 # Manually setting the primary key
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    release_date = models.DateField()
    label = models.CharField(max_length=40)
    description = models.TextField(max_length=300)

    def __str__(self):
        """ This function returns the string version of the
            class object."""
        return f"""{self.title}\n Released: {self.release_date}\n
                Label: {self.label}\n Description: {self.description}"""