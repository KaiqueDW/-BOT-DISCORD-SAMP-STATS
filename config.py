# =========================== [BIBLIOTECAS] ===========================

import discord
from discord.ext import commands

# =========================== [CONFIGURAÇÃO] ===========================

CONFIG = {
    'token': 'SEU_TOKEN_AQUI', # Coloque o Token do seu BOT
    'prefixo': '$$',  # Prefixo dos comandos do bot
    'server_ip': '127.0.0.1',  # IP do servidor SA:MP
    'server_port': 7777,  # Porta do servidor SA:MP
    'update_channel_id': 1234567890,  # Canal para envio de atualizações
    'embed_image_url': '',  # Imagem para embelezar os envios do bot
    'admin_tag': 'Staff',  # Tag para identificar administradores
    'admin_tag2': 'Helper',  # Tag para identificar helpers
    'footer_msg': 'Desenvolvido por Kaique_Rodrigues',  # Mensagem no rodapé dos embeds
    'arquivo': 'UltMensagem.ini'  # Arquivo para salvar o ID da última mensagem enviada
}

# =========================== [INTENTS DE PERMISSÕES] ===========================

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

# =========================== [SETANDO AS CONFIGURAÇÕES NA VARIÁVEL BOT] ===========================

bot = commands.Bot(command_prefix=CONFIG["prefixo"], intents=intents)

