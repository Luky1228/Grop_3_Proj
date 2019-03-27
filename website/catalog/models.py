from django.db import models


# Create your models here.
class GraphViz(models.Model):
    image = models.ImageField(blank=True, upload_to='catalog/Graphs')
    title = models.CharField(max_length=40, help_text="Year,, type")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.title


class GraphCreation(models.Model):
    year = models.IntegerField(choices=((2010, 2010),
                                        (2011, 2011),
                                        (2012, 2012),
                                        (2013, 2013),
                                        (2014, 2014),
                                        (2015, 2015),
                                        (2016, 2016),
                                        (2017, 2017),
                                        (2018, 2018),
                                        (2019, 2019)))
    graph = models.CharField(max_length=40, choices=(('A', 'Autors'),
                                                     ('C', 'Citations')))

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.year) + ' ' + self.graph

