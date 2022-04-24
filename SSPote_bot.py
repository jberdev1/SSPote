#-*- coding:latin-1 -*-
import discord
import sys
import random

ID_TEXT_CHANNEL = truc
ID_MESSAGE = machin
TOKEN = 'bidule'

LOGIN_MESSAGES = ["Quelqu'un est connecté sur l'ordinateur !", "Trop tard ! La station a été shotgun !", "La station est occupée, repasse plus tard !", 
                       "Il y a un membre de l'association d'audiovisuel de l'UTC sur cette station !"]
LOGOUT_MESSAGES = ["Il n'y a plus personne sur la station !", "La station est maintenant libre !", "La personne qui était sur cette station a quitté le poste !"
                          , "La station n'est plus occupée par personne !"]

botClient = discord.Client()


def delete_all_messages_except_one(msg):
    return msg.id != ID_MESSAGE


@botClient.event
async def on_ready():
    print('The bot is ready !')
    text_channel = await botClient.fetch_channel(ID_TEXT_CHANNEL)
    if(sys.argv[1] == 'connected'):
        await text_channel.purge(check = delete_all_messages_except_one)
        await text_channel.send(LOGIN_MESSAGES[random.randrange(4)])
    elif(sys.argv[1] == 'clean'):
        await text_channel.purge(check = delete_all_messages_except_one)
    elif(sys.argv[1] == 'disconnected'):
        await text_channel.send(LOGOUT_MESSAGES[random.randrange(4)])

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





