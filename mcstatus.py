import discord
import json
import requests
import asyncio

with open('config.json') as f:
    config = json.load(f)

TOKEN = config['token']
SERVER_IP = config['server_ip']
SERVER_NAME = config['server_name']
CHANNEL_ID = config['channel_id']

intents = discord.Intents.default()
intents.members = True 

client = discord.Client(intents=intents)

async def send_embedded_message():
    response = requests.get(f'https://api.mcsrvstat.us/2/{SERVER_IP}')
    if response.status_code == 200:
        data = response.json()
        if data['online']:
            player_names = ', '.join(data['players']['list']) if 'list' in data['players'] else 'No players online'
            num_players = data['players']['online']
            status = 'Online'
            color = 0x00ff00 # green
        else:
            player_names = 'Server offline'
            num_players = 0
            status = 'Offline'
            color = 0xff0000 # red

        embed = discord.Embed(title=f'{SERVER_NAME} Server Status', color=color)
        embed.add_field(name='Status:', value=status, inline=True)
        embed.add_field(name='Players Count:', value=num_players, inline=True)

        player_names_block = "```"
        for name in player_names:
            player_names_block += f"{name}"
        player_names_block += "```"
        embed.add_field(name='Players:', value=player_names_block, inline=False)
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(embed=embed)

async def background_task():
    await client.wait_until_ready()
    while True:
        await send_embedded_message()
        await asyncio.sleep(300)

@client.event
async def on_ready():
    print(f'{client.user} is online!')
    for guild in client.guilds:
        print(f'Connected to guild: {guild.name}, id: {guild.id}')
        for channel in guild.channels:
            print(f'Channel: {channel.name}, id: {channel.id}')
    client.loop.create_task(background_task())
client.run(TOKEN)
