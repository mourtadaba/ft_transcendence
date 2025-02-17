# models.py
from django.db import models
from django.conf import settings
from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, blank=True)
    blocked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='blocked_by', blank=True)
    
    def __str__(self):
        return self.user.username

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    is_game_invite = models.BooleanField(default=False)  # Ajout d'une valeur par défaut
    
    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.content
    
class GameInvite(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_invites', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_invites', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Declined')
    ], default='pending')

    class Meta:
        # Contrainte unique modifiée pour inclure le timestamp
        unique_together = ('sender', 'recipient', 'status', 'timestamp')
        indexes = [
            models.Index(fields=['sender', 'recipient', 'status'])
        ]
        
    def __str__(self):
        return f"{self.sender} -> {self.recipient} ({self.status})"

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tournaments')
    start_time = models.DateTimeField()
    
    def notify_next_players(self):
        # Logique pour notifier les prochains joueurs
        pass

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Connecter le signal
post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)