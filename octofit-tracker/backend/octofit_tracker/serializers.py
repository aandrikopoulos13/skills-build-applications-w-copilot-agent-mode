from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard
from bson import ObjectId

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if isinstance(rep.get('id'), ObjectId):
            rep['id'] = str(rep['id'])
        if rep.get('team') and isinstance(rep['team'].get('id'), ObjectId):
            rep['team']['id'] = str(rep['team']['id'])
        return rep

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = '__all__'
