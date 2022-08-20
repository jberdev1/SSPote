#-*- coding:latin-1 -*-
import discord
import sys
import random


ID_TEXT_CHANNEL = bidule
ID_MESSAGE = machin
TOKEN = 'truc'
LOGIN_MESSAGES = ["Quelqu'un est connecté sur l'ordinateur !", "Trop tard ! La station a été shotgun !", "La station est occupée, repasses plus tard !", 
                       "Il y a un membre de l'association d'audiovisuel de l'UTC sur cette station !"]
LOGOUT_MESSAGES = ["Il n'y a plus personne sur la station !", "La station est maintenant libre !", "La personne qui était sur cette station a quitté le poste !"
                          , "La station n'est plus occupée par personne !"]

WELCOME_MESSAGE = "Bienvenue sur le channel du bot SSP, viens ici pour savoir si la station est utilisée !"

botClient = discord.Client()


def delete_all_messages_except_one(msg):
    return msg.content != WELCOME_MESSAGE

def delete_test_messages(msg):
    print(msg.content)
    if ("test (ne pas prendre en compte) :" in msg.content):
        return True

def delete_all(msg):
    return True
	
@botClient.event
async def on_ready():
    print('The bot is ready !')
    text_channel = await botClient.fetch_channel(ID_TEXT_CHANNEL)
    if(sys.argv[1] == 'connected'):
        await text_channel.purge(check = delete_all_messages_except_one)
        await text_channel.send(random.choice(LOGIN_MESSAGES))
        print("")
    elif(sys.argv[1] == 'clean'):
        await text_channel.purge(check = delete_all_messages_except_one)
    elif(sys.argv[1] == 'disconnected'):
        await text_channel.send(random.choice(LOGOUT_MESSAGES))
        await text_channel.send("test : déconnection")
    elif(sys.argv[1] == 'test'):
        if(sys.argv[2] == 'connected'):
           await text_channel.purge(check = delete_test_messages)
           await text_channel.send("test (ne pas prendre en compte) : connection")
        else:
           await text_channel.send("test (ne pas prendre en compte) : deconnection")
    elif(sys.argv[1] == 'reset'):
          await text_channel.purge(check = delete_all)
          await text_channel.send(WELCOME_MESSAGE)
    print('Le message a ete envoye')
    await botClient.close()

@botClient.event
async def on_connect():
    print('connection etablished !') 

@botClient.event
async def on_disconnect():
    print('The client has been disconnected !')
    os._exit(0)

@botClient.event
async def on_error(event, *args, **kwargs):
    print(event)
    os._exit(-1)

print(sys.argv[1])
botClient.run(TOKEN)




