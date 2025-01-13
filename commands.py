import discord
from config import bot, CONFIG
from samp_client.client import SampClient

@bot.command(name="online")
async def online(ctx, *, nickname: str):
    server_ip = CONFIG['server_ip']
    server_port = CONFIG['server_port']

    if server_ip and server_port:
        try:
            with SampClient(address=server_ip, port=server_port) as client:
                if client.is_online():
                    detailed_clients = client.get_server_clients_detailed()
                    found_players = []
                    for player in detailed_clients:
                        if nickname.lower() in player.name.lower():
                            found_players.append(player)

                    if not found_players:
                        await ctx.send(f"Não encontrei nenhum jogador com '{nickname}' no nome.")
                        return

                    embed = discord.Embed(
                        title=f"🔍Buscando por '{nickname}'",
                        description="Aqui estão os jogadores que estão online com o nick:",
                        color=discord.Color.blue()
                    )

                    for player in found_players:
                        embed.add_field(name="Jogador", value=f"👤{player.name} - Level[{player.score}] Ping[{player.ping}]", inline=False)

                    embed.set_footer(
                        text=CONFIG['footer_msg']
                    )

                    # Envia o embed como resposta
                    await ctx.send(embed=embed)

                else:
                    await ctx.send(f"O servidor {server_ip}:{server_port} está offline.")
                    
        except Exception as e:
            print(f"Erro ao conectar ao servidor SA:MP: {str(e)}")
            await ctx.send(f"Erro ao conectar ao servidor SA:MP, tente novamente mais tarde.")
    else:
        await ctx.send("As informações do servidor não estão configuradas corretamente.")

@bot.command(name="players")
async def players(ctx):
    server_ip = CONFIG['server_ip']
    server_port = CONFIG['server_port']

    if server_ip and server_port:
        try:
            with SampClient(address=server_ip, port=server_port) as client:
                if client.is_online():
                    detailed_clients = client.get_server_clients_detailed()
                    found_players = []

                    for player in detailed_clients:
                        found_players.append(player)

                    # Se não encontrar ninguém, responde que não foi encontrado
                    if not found_players:
                        await ctx.send(f"O Servidor não possui ninguém online no momento.")
                        return

                    # Criar o embed para exibir os jogadores encontrados
                    embed = discord.Embed(
                        title=f"📊Jogadores online no servidor",
                        description="Aqui estão os jogadores que estão online no servidor:",
                        color=discord.Color.blue()
                    )

                    players_list = "\n".join([f"👤`{player.name}` - Level:[**{player.score}**] - Ping:[**{player.ping}**]" for player in found_players])
                    embed.add_field(name="Jogadores", value=players_list, inline=False)

                    embed.set_footer(
                        text=CONFIG['footer_msg']
                    )

                    # Envia o embed como resposta
                    await ctx.send(embed=embed)

                else:
                    await ctx.send(f"O servidor {server_ip}:{server_port} está offline.")
                    
        except Exception as e:
            print(f"Erro ao conectar ao servidor SA:MP: {str(e)}")
            await ctx.send(f"Erro ao conectar ao servidor SA:MP, tente novamente mais tarde.")
    else:
        await ctx.send("As informações do servidor não estão configuradas corretamente.")