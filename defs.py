import socket
from samp_client.client import SampClient
import sys
import configparser
from config import CONFIG

def localiniciado():
    hostname = socket.gethostname()
    endereco_ip = socket.gethostbyname(hostname)
    return endereco_ip

def get_adm_players(ip, port, admin_tag, admin_tag2):
    adm_players = []
    try:
        with SampClient(address=ip, port=port) as client:
            if client.is_online():
                detailed_clients = client.get_server_clients_detailed()
                for player in detailed_clients:
                    if admin_tag in player.name or admin_tag2 in player.name:
                        adm_players.append(player.name)
            else:
                print(f"Servidor {ip}:{port} está offline.")
    except Exception as e:
        print(f"Erro ao conectar no servidor SA:MP: {e}")
    return adm_players

def sistema_operacional():
    plataforma = sys.platform
    if plataforma.startswith('linux'):
        return 'Chrome OS' if 'chrome' in plataforma else 'Linux (ou distribuição Linux não especificada)'
    elif plataforma.startswith('darwin'):
        return 'MacOS'
    elif plataforma.startswith('win'):
        return 'Windows'
    elif 'iphone' in plataforma or 'ipad' in plataforma or 'ipod' in plataforma:
        return 'iOS'
    elif 'android' in plataforma:
        return 'Android'
    elif 'freebsd' in plataforma:
        return 'FreeBSD'
    elif 'openbsd' in plataforma:
        return 'OpenBSD'
    elif 'netbsd' in plataforma:
        return 'NetBSD'
    elif 'solaris' in plataforma:
        return 'Solaris'
    elif 'aix' in plataforma:
        return 'AIX'
    elif 'hp-ux' in plataforma:
        return 'HP-UX'
    elif 'irix' in plataforma:
        return 'IRIX'
    elif 'plan9' in plataforma:
        return 'Plan 9'
    elif 'haiku' in plataforma:
        return 'Haiku'
    elif 'reactos' in plataforma:
        return 'ReactOS'
    elif 'unixware' in plataforma:
        return 'UnixWare'
    elif 'qnx' in plataforma:
        return 'QNX'
    else:
        return 'Sistema operacional não reconhecido'

def get_samp_server_info(ip, port, admin_tag, admin_tag2):
    try:
        with SampClient(address=ip, port=port) as client:
            info = client.get_server_info()
            staff_players = get_adm_players(ip, port, admin_tag, admin_tag2)
            return {
                "hostname": info.hostname,
                "players": info.players,
                "max_players": info.max_players,
                "gamemode": info.gamemode,
                "staff_online": staff_players  # Retorna os jogadores com as tags configuradas
            }
    except Exception as e:
        print(f"Erro ao conectar no servidor SA:MP: {e}")
        return None

def salvar(channel_id, message_id):
    config = configparser.ConfigParser()
    config['MSG_ANTIGA'] = {'channel_id': str(channel_id), 'message_id': str(message_id)}
    with open(CONFIG['arquivo'], 'w') as file:
        config.write(file)

# Essa função carregará o ID da ultima mensagem enviada pelo BOT sobre a Estátisticas do servidor.
def carregar():
    config = configparser.ConfigParser()
    config.read(CONFIG['arquivo'])
    if 'MSG_ANTIGA' in config:
        return config['MSG_ANTIGA'].get('channel_id'), config['MSG_ANTIGA'].get('message_id')
    return None, None