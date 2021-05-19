
# libs
import discord
import random, re, sys

# globals
PREFIX = r"!"
TOKEN = str(open("../TOKEN", "r").readlines()[0].strip("\n"))
INVITE = "https://discordapp.com/oauth2/authorize?client_id=844685330241159170&permissions=8&scope=bot"

# colors
BLUE = 0x023059
GOLD = 0xf2c84b

# client
class MyClient(discord.Client):
	
	# logged in
	async def on_ready(self):
		print("logged in")
	
	# recognize command
	async def on_message(self, message):
		if message.author != client.user and message.content.startswith(PREFIX):
			
			# roll command
			if re.search(rf"{PREFIX}roll +[0-9]+d[0-9]+(\*[0-9]+)?", message.content):
				# extract dice data
				msg = f"{message.content}*1"
				count = int(msg.split("d")[0].split(" ")[1])
				faces = int(msg.split("d")[1].split("*")[0])
				factor = int(msg.split("d")[1].split("*")[1])
				# generate dice roll and result
				roll = [ random.randint(1, faces) for _ in range(count) ]
				result = sum(roll) * factor
				# create embed
				embed = discord.Embed(title="Alea iacta est", color=BLUE)
				embed.add_field(name="User", value=f"`{message.author.name}#{message.author.discriminator}`", inline=False)
				embed.add_field(name="Roll", value=f"`{roll}`", inline=False)
				embed.add_field(name="Result", value=f"`{result}`", inline=False)
				await message.channel.send(embed=embed)
			
			# info command
			elif re.search(rf"{PREFIX}info", message.content):
				# create embed
				embed = discord.Embed(title="Info", color=BLUE)
				embed.set_thumbnail(url=str(client.user.avatar_url))
				embed.add_field(name="Usage", value=f"`{PREFIX}roll 2d6*3` can return for example `Roll: [4, 5]` and `Result: 27`", inline=False)
				embed.add_field(name="GitHub", value=r"https://github.com/InformaticFreak/QuantumDice", inline=False)
				embed.add_field(name="Invite", value=INVITE, inline=False)
				await message.channel.send(embed=embed)

# run
client = MyClient()
client.run(TOKEN)
