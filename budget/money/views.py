from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Expense, Income, Remain
from .serializers import ExpenseSerializer, IncomeSerializer, RemainSerializer


class ExpenseAPIView(APIView):

    def get(self, request):
        user = Expense.objects.filter(user=request.data['user'])
        return Response({"data": ExpenseSerializer(user, many=True).data})

    def post(self, request):
        expense = ExpenseSerializer(data=request.data)
        if expense.is_valid(raise_exception=True):
            Expense.objects.create(
                user_id=expense.data.get("user"),
                comment=expense.data.get("comment"),
                amount=expense.data.get("amount"),
            )
            remain = Remain.objects.get(user_id=expense.data.get("user")).quantity
            result = remain - expense.data.get("amount")
            Remain.objects.filter(user_id=expense.data.get("user")).update(quantity=result)

            return Response({"data": expense.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        expense = Expense.objects.get(pk=pk)
        remain = Remain.objects.get(user_id=expense.user).quantity
        result = remain + expense.amount
        Remain.objects.filter(user_id=expense.user).update(quantity=result)
        expense.delete()
        return Response({"data": 'delete'})


class IncomeAPIView(APIView):

    def get(self, request):
        user = Income.objects.filter(user=request.data['user'])
        return Response({"data": IncomeSerializer(user, many=True).data})

    def post(self, request):
        income = IncomeSerializer(data=request.data)
        if income.is_valid(raise_exception=True):
            Income.objects.create(
                user_id=income.data.get("user"),
                comment=income.data.get("comment"),
                amount=income.data.get("amount"),
            )
            remain = Remain.objects.get(user_id=income.data.get("user")).quantity
            result = remain + income.data.get("amount")
            Remain.objects.filter(user_id=income.data.get("user")).update(quantity=result)

            return Response({"data": income.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        income = Income.objects.get(pk=pk)
        remain = Remain.objects.get(user_id=income.user).quantity
        result = remain - income.amount
        Remain.objects.filter(user_id=income.user).update(quantity=result)
        income.delete()
        return Response({"data": 'delete'})


class RemainAPIView(APIView):

    def get(self, request):
        user = Remain.objects.filter(user=request.data['user'])
        return Response({"data": RemainSerializer(user, many=True).data})
