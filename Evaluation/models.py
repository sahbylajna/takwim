from django.db import models

class Evaluation(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    notes = models.TextField()
    etat = models.TextField()
    evaluator_id = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    RATING_CHOICES = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    )
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)

    client_id = models.ForeignKey('Client.ClientUser',related_name='client_evaluations', on_delete=models.CASCADE)  # Replace 'YourClientModel' with your actual client model
    evaluator_id = models.ForeignKey('Client.ClientUser',related_name='respo_evaluations', on_delete=models.CASCADE)  # Replace 'YourClientModel' with your actual client model
