# # # # # # # # # # # # # # # # # # # # # # # # # # # # #  # # # # # # # # # # # 
#               DISCORD BOT SAMP STATUS                                         #
#  > Desenvolvido por Kaique_Rodrigues                                          #
#  > Requisitos: Python 3.6                                                     #  
#  > Essa é uma versão que eu criei antes de adicionar o banco de dados SQL     #
#               DISCORD BOT SAMP STATUS                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #  # # # # # # # # # # # 


from config import bot, CONFIG
import commands
import callbacks

if __name__ == "__main__":
    bot.run(CONFIG['token'])
