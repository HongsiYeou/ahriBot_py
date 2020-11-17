#pip install -U discord.py
import json

import discord
#pip install requests
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    #유저조회 중복 방지
    if message.author.bot:
        return

    if "♥" in message.content:
        if message.content.startswith('♥매혹요청'):
            if "$" in message.content:
                await  message.channel.send('```저랑 놀려면, 게임을 아주 잘 하셔야 돼요...후훗....```')

                await message.channel.send(message.content)
                userName = message.content.split("$")[1]

                userData = getUserData(userName)

                e = discord.Embed(title=userData['userName'])
                e.set_author(name = "매혹 결과...♥")
                e.set_thumbnail(url=userData["userImage"])

                for item in userData["result"]:
                    Game = item["ChampName"] + " [ " + item["GameResult"]+" ] "
                    KDA = "킬 : "+item["Kill"] + "\t|\t" + "데스 : "+ item["Death"] + "\t|\t" + "어시스트 : "+ item["assist"]
                    e.add_field(name=Game, value=KDA, inline=False)

                await message.channel.send(userName, embed = e)

                getUserData(userName)
            else:
                await message.channel.send('```매혹을 실패했어요 ㅠ.```')
                await message.channel.send('♥유저조회$<유저명>')
        elif message.content.startswith('♥help'):
            await message.channel.send('```[우흐흣..]\n\n명령어 : \n♥매혹요청$[롤 닉네임] \nUser의 10판의 전적을 검색합니다. \n\n==ㅁ==ㅁ==♥==ㅁ==ㅁ==-[ 예시 ]-==ㅁ==ㅁ==♥==ㅁ==ㅁ==\n|\n|                ♥매혹요청$아리봇 \n|\n==ㅁ==ㅁ==ㅁ==ㅁ==ㅁ==[ 예시 ]==ㅁ==ㅁ==ㅁ==ㅁ==ㅁ==```')
        elif message.content.startswith('!?'):
            await message.channel.send('https://tenor.com/view/umm-confused-blinking-okay-white-guy-blinking-gif-7513882')
        elif message.content.startswith('♥매혹'):
            await message.channel.send('```"가슴이 더 뛰게 해 줄까? 아님... 멈추게 해 줄까...♥"```')
        else:
            await message.channel.send('명령어를 재대로 입력해주세요')


def getUserData (userName):
    response = requests.get("http://3964bf147c56.ngrok.io/?name="+userName)

    json_val = response.json()
    return json_val

client.run('token')
