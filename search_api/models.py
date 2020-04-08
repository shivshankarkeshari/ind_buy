from django.db import models

# Create your models here.
CHOICE_FIELD = [
    ('spam', 'spam'),
    ('not-spam', 'not-spam')
]


class CuniqueData(models.Model):
    message = models.TextField()
    truth = models.CharField(max_length=10, choices=CHOICE_FIELD, blank=True, null=True)
    cube = models.CharField(max_length=10, choices=CHOICE_FIELD, blank=True, null=True)
    google = models.CharField(max_length=10, choices=CHOICE_FIELD, blank=True, null=True)
    ibm = models.CharField(max_length=10, choices=CHOICE_FIELD, blank=True, null=True)
    google_spam = models.DecimalField(max_digits=22, decimal_places=6, blank=True, null=True)
    google_not_spam = models.DecimalField(max_digits=22, decimal_places=6, blank=True, null=True)
    ibm_spam = models.DecimalField(max_digits=22, decimal_places=6, blank=True, null=True)
    ibm_not_spam = models.DecimalField(max_digits=22, decimal_places=6, blank=True, null=True)



