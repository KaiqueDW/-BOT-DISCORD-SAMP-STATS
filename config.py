# =========================== [BIBLIOTECAS] ===========================

import discord
from discord.ext import commands

# =========================== [CONFIGURAÇÃO] ===========================

CONFIG = {
    'token': 'SEU_TOKEN_AQUI',
    "prefixo": "$$",
    'server_ip': '127.0.0.1',
    'server_port': 7777,
    'update_channel_id': 1234567890,  # ID do canal para envio de atualizações
    'embed_image_url': '', #Imagem que aparecerá quando o BOT enviar o status do servidor
    'admin_tag': 'Staff',
    'admin_tag2': 'Helper',
    'footer_msg': 'Desenvolvido por Kaique_Rodrigues',
    'arquivo': 'UltMensagem.ini' #Essa função salvará o ID da ultima mensagem enviada pelo BOT sobre a Estátisticas do servidor.
}

# =========================== [INTENTS DE PERMISSÕES] ===========================

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

# =========================== [SETANDO AS CONFIGURAÇÕES NA VARIÁVEL BOT] ===========================

bot = commands.Bot(command_prefix=CONFIG["prefixo"], intents=intents)

