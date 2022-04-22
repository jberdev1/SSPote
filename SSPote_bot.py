#-*- coding:latin-1 -*-
import discord
import sys
import random

ID_TEXT_CHANNEL = 953967217534459934
ID_MESSAGE = 954281307284860978
TOKEN = 'OTUzOTYwNTU4NDM1MTEwOTIy.YjMLAA.16MrhuXxNPMmwIhw5do3LrJSSuQ'

LOGIN_MESSAGES = {"Quelqu'un est connect� sur l'ordinateur !", "Trop tard ! La station a �t� shotgun !", "La station est occup�e, repasse plus tard !", 
                       "Il y a un membre de l'association d'audiovisuel de l'UTC sur cette station !"}
LOGOUT_MESSAGES = {"Il n'y a plus personne sur la station !", "La station est maintenant libre !", "La personne qui �tait sur cette station a quitt� le poste !"
                          , "La station n'est plus occup�e par personne !"} 

botClient = discord.Client()


def delete_all_messages_except_one(msg):
    return msg.id != ID_MESSAGE


@botClient.event
async def on_ready():
    print('The bot is ready !')
    text_channel = await botClient.fetch_channel(ID_TEXT_CHANNEL)
    if(sys.argv[1] == 'connected'):
        await text_channel.purge(check = delete_all_messages_except_one)
        await text_channel.send(LOGIN_MESSAGES[random.randrange(3)])
    elif(sys.argv[1] == 'clean'):
        await text_channel.purge(check = delete_all_messages_except_one)
    elif(sys.argv[1] == 'disconnected'):
        await text_channel.send(LOGOUT_MESSAGES[random.randrange(3)])

    print('Le message a ete envoye')
    await botClient.close()
    print('The bot is disconnected !')


@botClient.event
async def on_connect():
    print('connection etablished !') 

@botClient.event
async def on_disconnect():
    print('The client has disconnected !')


print(sys.argv[1])
botClient.run(TOKEN)




