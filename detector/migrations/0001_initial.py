from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
 initial=True
 dependencies=[('auth','0012_alter_user_first_name_max_length')]
 operations=[migrations.CreateModel(name='URLPrediction',fields=[
 ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
 ('url',models.URLField(max_length=2000)),('prediction',models.CharField(max_length=20)),
 ('confidence',models.FloatField(default=0)),('risk_level',models.CharField(max_length=20)),
 ('created_at',models.DateTimeField(auto_now_add=True)),
 ('user',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,to='auth.user'))])]
