from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Plan
from .serializer import PlanSerializer, PromoSerializer, UserSelectedPlansSerializer

@api_view(['GET'])
def get_plans(request):
    # plans = Plan.objects.all()
    queryset = Plan.objects.prefetch_related('promos').all()
    serializer = PlanSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_plan(request):
    serializer = PlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(request.data, status.HTTP_201_CREATED)
    return Response(request.data, status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_plan(request, planID):
    try:
        plan = Plan.objects.get(pk=planID)
    except Plan.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    plan.delete()
    return Response(status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_promo(request):
    serializer = PromoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(request.data, status.HTTP_201_CREATED)
    return Response(request.data, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_selected_plan_entry(request):
    serializer = UserSelectedPlansSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(request.data, status.HTTP_201_CREATED)
    return Response(request.data, status.HTTP_400_BAD_REQUEST)