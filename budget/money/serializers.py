from rest_framework import serializers
from .models import Income, Remain, Expense


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"


class RemainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remain
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"
