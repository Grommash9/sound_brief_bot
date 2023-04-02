from django.db import models


class User(models.Model):
    user_id = models.BigIntegerField(unique=True, null=False, primary_key=True)
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=150, blank=True, null=True)
    balance = models.FloatField(default=0)

    class Meta:
        db_table = "data_tg_user"
        verbose_name_plural = 'Користувачі бота'

    def __str__(self):
        return f"{self.user_id} {self.user_name}"


class MessageToProcess(models.Model):
    record_id = models.AutoField(unique=True, null=False, primary_key=True)
    message_id = models.BigIntegerField()
    chat_id = models.BigIntegerField()
    text = models.CharField(max_length=5000, null=True, blank=True)
    short_text = models.CharField(max_length=5000, null=True, blank=True)
    sent = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "voice_files"
        verbose_name_plural = 'Голосовые файлы'

