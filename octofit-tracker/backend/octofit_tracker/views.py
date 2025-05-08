from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://symmetrical-parakeet-q745699xxhrwj-8000.app.github.dev/'
    return Response({
        'users': base_url + 'api/users/',
        'teams': base_url + 'api/teams/',
        'activity': base_url + 'api/activity/',
        'leaderboard': base_url + 'api/leaderboard/',
        'workouts': base_url + 'api/workouts/',
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
