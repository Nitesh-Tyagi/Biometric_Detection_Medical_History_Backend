from django.db import models

class BMPImage(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    patient_name = models.CharField(max_length=50, blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    patient_gender = models.CharField(max_length=50, blank=True, null=True)
    patient_hand = models.CharField(max_length=50, blank=True, null=True)
    patient_finger = models.CharField(max_length=50, blank=True, null=True)
    patient_height = models.IntegerField(blank=True, null=True)
    patient_weight = models.IntegerField(blank=True, null=True)
    match_value = models.IntegerField(blank=True, null=True)
