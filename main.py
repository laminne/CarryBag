# -*- coding: utf-8 -*-
import asyncio
import discord
import subprocess
import os
import requests
from urllib.parse import urljoin
import sqlite3
client = discord.Client()
conn = sqlite3.connect('meigen.db')
c = conn.cursor()

async def send(channel,*args, **kwargs): return await channel.send(*args, **kwargs)
 
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '!Carry':
        await message.channel.send("登録します メッセージを続けて入力してください")

        def check(command):
            return command.author == message.author
        cc = await client.wait_for("message", check=check)

        meigen = cc.content
        sql = 'insert into meigen (body) values (?)'
        namelist = (meigen)
        c.execute(sql, namelist)
        conn.commit()


    if message.content == '!Carry search':
        await message.channel.send("検索します 名言IDを続けて入力して下さい")

        def check(command):
            return command.author == message.author
        cc = await client.wait_for("message", check=check)

        id = cc.content
        select_sql = 'select * from meigen where id='
        id = ('{id}').format(id=id)
        select_sql = select_sql + id
        print(select_sql)
        c.execute(select_sql)
        result = c.fetchone()
        m = result[1]
        await message.channel.send(m)
if __name__ == "__main__":
    client.run(os.environ['MEIGEN_TOKEN'])