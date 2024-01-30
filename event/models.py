from django.db import models



# Create your models here.

class PrivateEvent(models.Model):
    treated_user = models.CharField(max_length=155)
    point_of_contact = models.ForeignKey('users.User', on_delete=models.CASCADE)
    description = models.TextField()
    tier = models.IntegerField()
    estimated_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        permissions = (
            ("cannot_view_private_event", "Cannot view private event"),
            ("can_edit_private_event", "Can edit private event"),
        )
    
    def __str__(self):
        return self.treated_user
    

class InviteEvent(models.Model):
    private_event = models.ForeignKey(PrivateEvent, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    accepted = models.BooleanField(default=False)
    percentage_of_cost = models.IntegerField()
    event_amount = models.IntegerField()
    
    
    def __str__(self):
        return str(self.private_event) | str(self.email)