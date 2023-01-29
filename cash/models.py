from django.db import models
from django.db.models.signals import post_save
from django.shortcuts import redirect


class Currency(models.Model):
    """
    Cash model with price and type cash
    """
    type = models.CharField(max_length=20)
    rate = models.FloatField(max_length=20)

    def __str__(self):
        return self.type


class Query(models.Model):
    """
    Converter, user give information what tyoe of cash gives and how many
    """
    give = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, blank=True, related_name='currency_from')
    value = models.IntegerField()
    order = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, blank=True, related_name='currency_to')

    def __str__(self):
        return str(self.give)


class Answer(models.Model):
    """
    Auto add after create Query. Answer for user
    """
    type = models.CharField(max_length=10)
    value = models.FloatField(max_length=10)
    conversation_rate = models.FloatField(max_length=10)


def post_query_save(sender, instance, created, *args, **kwargs):
    """
    Create answer after query saved.
    """
    if created:
        currency_from = Currency.objects.get(type=instance.give)
        currency_to = Currency.objects.get(type=instance.order)
        Answer.objects.create(type=instance.order,
                              value=((currency_from.rate * instance.value) / currency_to.rate).__round__(2),
                              conversation_rate=(currency_from.rate / currency_to.rate).__round__(2))

    return redirect("answer/", args=())


post_save.connect(post_query_save, sender=Query)
