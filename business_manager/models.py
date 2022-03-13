from django.db import models
from django.contrib.auth import get_user_model
from django.db import transaction
from django.core.exceptions import ValidationError , BadRequest


User = get_user_model()


class SysTransaction(models.Model):

    provider = models.ForeignKey(User,on_delete=models.PROTECT,related_name="outgoing_Transaction")
    consumer = models.ForeignKey(User,on_delete=models.PROTECT,related_name="incoming_Transaction")
    amount  = models.BigIntegerField()
    date = models.DateTimeField(auto_now=True)
    status =  models.CharField(max_length=256,blank=True)


    def save(self,*args, **kwargs) -> None:
        if self.pk:
            raise ValidationError("Transactions are not editable")
        if self.provider == self.consumer:
            raise ValidationError("porvider and consumer cant be same")
        try:
            with transaction.atomic():
                provider = User.objects.select_for_update().get(pk=self.provider.pk)
                consumer = User.objects.select_for_update().get(pk=self.consumer.pk)
                consumer.update_credit(self.amount)
                provider.update_credit(-(self.amount))
                self.status = "successful"

        except Exception as erorr :
            self.status = erorr

        finally:
            return super().save(*args, **kwargs)

    def delete(self):
        raise BadRequest("transactions are not deletable")

    def __str__(self) -> str:
        return f"porvider: {self.provider}, consumer:{self.consumer}, date:{self.date}"

