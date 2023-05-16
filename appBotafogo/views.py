from django.shortcuts import render, redirect 
from .models import BotafogoJogos, BotafogoVitórias, Task
#Este trecho importa as funções render e redirect do módulo django.shortcuts e os modelos BotafogoJogos, BotafogoVitórias e Task do arquivo models.py.

# Create your views here.
def atividade1(request):
  return render(request,"atividade1.html") #A função atividade1 recebe um objeto request do Django e retorna o resultado da função render, que renderiza o modelo HTML "atividade1.html".

def list_games(request):
  games= BotafogoJogos.objects.all()
  wins= BotafogoVitórias.objects.all()
  context={"games": games}
  return render(request,"atividade1.html")
  #A função list_games também recebe um objeto request do Django. Ela obtém todos os objetos do modelo BotafogoJogos e BotafogoVitórias usando a função all() e armazena-os nas variáveis games e wins. Em seguida, cria um dicionário chamado context com a chave "games" e o valor games. Por fim, a função retorna o resultado da função render, que renderiza o modelo HTML "atividade1.html" sem passar o dicionário context para o modelo.

def list_wins(request):
  games= BotafogoJogos.objects.all()
  wins=  BotafogoVitórias.objects.all()
  context={"wins" : wins}
  return render(request,"lista.html",context=context)
  #Esta função list_wins também recebe um objeto request do Django. Ela obtém todos os objetos do modelo BotafogoJogos e BotafogoVitórias usando a função all() e armazena-os nas variáveis games e wins. Em seguida, cria um dicionário chamado context com a chave "wins" e o valor wins. Por fim, a função retorna o resultado da função render, que renderiza o modelo HTML "lista.html", passando o dicionário context para o modelo.
  
def create_task(request):
  if request.method=="POST":
    print(request.POST["title"])
    Task.objects.create(
      title=request.POST["title"],
      description=request.POST["description"],
      due_date=request.POST["due-date"],
      done=False
    )
    return redirect("list_games")
    
  return render (request,"tarefas.html") #Esta função create_task também recebe um objeto request do Django. Ela verifica se o método da requisição é "POST" usando request.method == "POST". Se for verdadeiro, cria um novo objeto do modelo Task com os dados do formulário recebidos em request.POST. Em seguida, redireciona o usuário para a view chamada "list_games" usando a função redirect. Se o método da requisição não for "POST", a função renderiza o modelo HTML "tarefas.html".

def update_task(request,id):
  task = Task.objects.get(id=id)
  task.due_data=task.due_date.strftime('%Y-%m-%d')
  if request.method == "POST":      
    task.title=request.POST['title']
    task.description=request.POST["description"],
    task.due_date=request.POST["due-date"],
    if 'done' not in request.POST:
      task.done=False
    else:
      task.done=True
    
    task.save()
    return render(request,'tarefas.html',
    {"task":task}) #Define uma função chamada update_task que recebe um objeto request e um parâmetro id, Formata a data de vencimento pra formato %Y-%m-%d, salva a tarefa atualizada no banco de dados

  
    
 

def delete_task(request,id):
  task=Task.objects.get(id=id)
  if request.method=='POST':
    task.delete
  pass #Define uma função chamada delete_task que recebe um objeto request e um parâmetro id, verifica se o método da requisição é POST , caso seja, chama o método delete para excluir a tarefa do banco de dados

