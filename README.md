# 🛡️ BOT-DISCORD-SAMP-STATS: Mantenha sua comunidade informada sobre seu servidor!

O **SAMP-STATS** é um bot avançado para Discord desenvolvido para integrar informações de servidores SA:MP diretamente no seu servidor Discord. Com ele, você pode visualizar detalhes do servidor em tempo real, buscar jogadores online, monitorar administradores conectados, e muito mais – tudo de forma automática e personalizável.

---

## ✨ **O que o SAMP-STATS faz?**

### Funcionalidades principais:
- **📊 Informações do servidor:** O bot exibe o nome do servidor, número de jogadores online, limite de jogadores, ping, modo do servidor e versão.
- **🔍 Busca de jogadores:** Encontre jogadores específicos que estejam online com base no nome ou tags configuradas.
- **🛠️ Monitoramento de administradores:** Detecta automaticamente administradores e helpers online.
- **📬 Atualizações automáticas:** Envia informações do servidor periodicamente em um canal específico.
- **🗂️ Configurações fáceis:** Configure o token, IP do servidor, canal de atualizações e muito mais em um único arquivo.
- **🌟 Responde á palavra chave "ip":**  Responde à palavra **`ip`** no chat com o IP e porta configurados do servidor.
  
---

## 🚀 **Como instalar e configurar o BOT**

### **1. Requisitos**
Para que o bot funcione corretamente, você precisa:
- Python 3.8 a 3.12 (compatível com versões anteriores com ajustes nos "Intents").
- Conexão com a Internet (Wi-Fi ou cabo).
- Permissões adequadas no Discord (como gerenciar mensagens e ver canais).

---

### **2. Instalar dependências**
Todas as bibliotecas necessárias estão listadas no arquivo `requirements.txt`.

**Passos para instalação:**
1. Certifique-se de que o Python e o pip estão instalados.
2. No terminal (ou no terminal do VSCode), navegue até o diretório do bot.
3. Execute o comando:
   ```bash
   pip install -r requirements.txt
   ```
4. Confirme que nenhuma biblioteca apresentou erros durante a instalação.

---

### **3. Configurar o bot**
As configurações são feitas no arquivo `config.py`. Esse arquivo contém todas as opções principais do bot:

```python
'prefixo': '$$',  # Prefixo dos comandos do bot
'server_ip': '127.0.0.1',  # IP do servidor SA:MP
'server_port': 7777,  # Porta do servidor SA:MP
'update_channel_id': 1234567890,  # Canal para envio de atualizações
'embed_image_url': '',  # Imagem para embelezar os envios do bot
'admin_tag': 'Staff',  # Tag para identificar administradores
'admin_tag2': 'Helper',  # Tag para identificar helpers
'footer_msg': 'Desenvolvido por Kaique_Rodrigues',  # Mensagem no rodapé dos embeds
'arquivo': 'UltMensagem.ini'  # Arquivo para salvar o ID da última mensagem enviada
```

💡 **Dica:** Os comentários explicam o que cada configuração faz, facilitando qualquer alteração.

---

## 🔧 **Comandos disponíveis**

- **`$$players`**: Mostra todos os jogadores online no servidor SA:MP.
- **`$$online [nome]`**: Busca por um ou mais jogador online no servidor.

---


## 🤝 **Contribuindo**
Este bot foi projetado para ser fácil de entender e personalizar. Sinta-se à vontade para contribuir com melhorias ou relatar problemas abrindo uma [issue](https://github.com/seu-usuario/repositorio/issues) ou enviando um pull request.

---

## 📜 **Licença**
Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

**Desenvolvido com ❤️ por Kaique_Rodrigues**
