from django.db import models

# Create your models here.
class SlotStatus(models.Model):

    device_id = models.TextField(max_length=200,primary_key=True)
    slot_1    = models.IntegerField(choices=((0,0),(1,1)),default=0)
    slot_2    = models.IntegerField(choices=((0,0),(1,1)),default=0)

    def __str__(self):
        return self.device_id