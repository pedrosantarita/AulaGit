from django.contrib import admin #Importa o módulo admin do Django para registrar os modelos no painel de administração.

# Register your models here.
from .models import BotafogoJogos
from .models import BotafogoVitórias #Importa os modelos BotafogoJogos e BotafogoVitórias do arquivo models.py do diretório atual.

admin.site.register(BotafogoJogos)
admin.site.register(BotafogoVitórias) #Registra os modelos BotafogoJogos e BotafogoVitórias no painel de administração, permitindo que os modelos sejam gerenciados e exibidos no painel de administração do Django, fornecendo uma interface para visualizar, criar, editar e excluir registros desses modelos.


#python3 manage.py createsuperuser