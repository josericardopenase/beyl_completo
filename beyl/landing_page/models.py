from django.db import models

class Plan(models.Model):

    name = models.CharField(max_length=255)
    price = models.FloatField(null = True, blank=True)
    highlight = models.BooleanField()
    max_peaple = models.IntegerField(null = True, blank=True)
    contact = models.BooleanField()

    def __str__(self):
        return self.name

class PlanInclude(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='features')
    enable = models.BooleanField()
    feature = models.ForeignKey('landing_page.PlanFeature', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.enable) + " " + self.feature.text

class PlanFeature(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


