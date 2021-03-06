from rest_framework import serializers

from .models import User, Todo, Habit, Goal, Check


class CheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Check
        fields = ['id', 'habit', 'timestamp']


class TodoSerializer(serializers.ModelSerializer):
    dueTime = serializers.TimeField("%H:%M")
    class Meta:
        model = Todo
        fields = ['id', 'description', 'xp', 'user', 'completed', 'dueDate', 'dueTime']


class HabitSerializer(serializers.ModelSerializer):
    checks = CheckSerializer(many=True, required=False)

    class Meta:
        model = Habit
        fields = ['id', 'description', 'multiplier', 'user', 'checks']


class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = ['id', 'description', 'xp', 'completed', 'user', 'timePeriod']


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, required=False)
    habits = HabitSerializer(many=True, required=False)
    goals = GoalSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'level', 'username', 'level', 'xp',
                  'xp_to_lvlup', 'todos', 'habits', 'goals']
