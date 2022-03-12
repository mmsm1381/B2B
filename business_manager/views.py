from django.db.models import Q

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import SysTransaction
from .serializers import SysTransactionSerializer



class TransactionAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    model = SysTransaction
    serializer_class = SysTransactionSerializer

    def get_queryset(self):
        user = self.request.user
        return SysTransaction.objects.filter(Q(provider=user)|Q(consumer=user))