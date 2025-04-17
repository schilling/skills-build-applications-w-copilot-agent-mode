from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users 
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Create test activities
        Activity.objects.create(user=user1, activity_type='running', duration=timedelta(minutes=30))
        Activity.objects.create(user=user2, activity_type='cycling', duration=timedelta(hours=1))

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, score=150)
        Leaderboard.objects.create(user=user2, score=200)

        # Create test workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing morning yoga session')
        Workout.objects.create(name='HIIT', description='High-intensity interval training')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
