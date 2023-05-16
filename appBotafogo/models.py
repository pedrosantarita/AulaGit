from django.db import models #Importa o módulo models do Django para criar modelos de banco de dados.

# Create your models here.
class BotafogoJogos(models.Model):
  título = models.CharField(max_length = 50)
  números = models.TextField()
  tipo = models.TextField()
  história = models.BooleanField() #Define uma classe chamada BotafogoJogos que herda da classe models.Model,Cria campos para representar as informações dos jogos do Botafogo.

class BotafogoVitórias(models.Model):
  título = models.CharField(max_length = 50)
  time = models.TextField()
  vitórias = models.TextField()
  esseano = models.BooleanField() #Define uma classe chamada BotafogoVitórias que herda da classe models.Model,Cria campos para representar as informações das vitórias do Botafogo.

class Task(models.Model):
  title = models.CharField(max_length = 50)
  description = models.TextField()
  due_date = models.DateField()
  done = models.BooleanField() #Define uma classe chamada Task que herda da classe models.Model, cria campos para representar as informações da tarefa.
