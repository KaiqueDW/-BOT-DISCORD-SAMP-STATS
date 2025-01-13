# =============== [BIBLIOTECAS E MODULOS] =======================

import discord
from discord.ext import tasks
from config import bot, CONFIG
from defs import get_samp_server_info, localiniciado, sistema_operacional, carregar, salvar
from datetime import datetime
import sys
import re


@tasks.loop(minutes=1)
async def send_samp_update():
    channel = bot.get_channel(CONFIG['update_channel_id'])
    if channel:
        server_info = get_samp_server_info(CONFIG['server_ip'], CONFIG['server_port'], CONFIG['admin_tag'], CONFIG['admin_tag2'])
        if server_info:
            now = datetime.now()
            time_str = now.strftime("%H:%M")

            embed = discord.Embed(
                title="🌐**Informações do Servidor SA:MP**",
                color=discord.Color.blue()
            )
            embed.add_field(name="🕘Atualizado as:", value=time_str, inline=False)
            embed.add_field(name="💬Hostname", value=server_info["hostname"], inline=False)
            embed.add_field(name="📌IP do Servidor", value=f"{CONFIG['server_ip']}:{CONFIG['server_port']}", inline=False)
            embed.add_field(name="👥Players Online", value=f"{server_info['players']}/{server_info['max_players']}", inline=True)
            embed.add_field(name="🎮Gamemode", value=server_info["gamemode"], inline=True)
            embed.add_field(name=f"💼Admins Online", value="\n".join(server_info["staff_online"]) if server_info["staff_online"] else "Nenhum admin online", inline=False)
            embed.set_footer(text=CONFIG['footer_msg'])
            if CONFIG['embed_image_url']:
                embed.set_image(url=CONFIG['embed_image_url'])

            # Deletar a última mensagem enviada
            canal_id, antiga = carregar()
            if canal_id == str(CONFIG['update_channel_id']) and antiga:
                try:
                    antiga_msg = await channel.fetch_message(int(antiga))
                    await antiga_msg.delete()
                except:
                    pass

            msg = await channel.send(embed=embed)
            salvar(CONFIG['update_channel_id'], msg.id)

@bot.event
async def on_ready():
    ip = localiniciado()
    system = sistema_operacional()
    send_samp_update.start()
    print('BOT Carregado com sucesso')
    print(f"Nome do BOT: {bot.user}")
    print(f"Versão do Python do Hoster: {sys.version}")
    print(f"Hoster está utilizando o sistema operacional: {system}")
    print(f"Endereço IP do dispositivo: {ip}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    
    if re.search(r'\bip\b', message.content, re.IGNORECASE):
        server_ip = CONFIG['server_ip']
        server_port = CONFIG['server_port']
        if server_ip and server_port:
            await message.channel.send(f"O IP do servidor é `{server_ip}:{server_port}`")
        else:
            await message.channel.send("As informações do servidor não estão configuradas corretamente.")
    
    await bot.process_commands(message)
