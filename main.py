
# libs
import discord
import secrets, re
import time, datetime, logging

# globals
PREFIX = r"!"
TOKEN = str(open(r"../TOKEN", "r").readlines()[0].strip("\n"))
INVITE = r"https://discordapp.com/oauth2/authorize?client_id=844685330241159170&permissions=8&scope=bot"

# colors
BLUE = 0x023059
GOLD = 0xf2c84b

# logging
logging.basicConfig(filename=r"dice_rolls.log", level=logging.INFO, format="%(levelname)s;%(asctime)s;%(message)s", datefmt="%m/%d/%Y;%I:%M:%S")

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
				roll = [ secrets.randbelow(faces)+1 for _ in range(count) ]
				result = sum(roll) * factor
				# log dice roll
				logging.info("{message};{author};{result};{roll}".format(
					message=message.content.replace(r"\n", r"\\n"),
					author=f"{message.author.name}#{message.author.discriminator}",
					result=result,
					roll=";".join([ str(num) for num in roll ]))
				)
				# create embed
				embed = discord.Embed(title="Alea Iacta Est", color=BLUE)
				embed.add_field(name="User", value=f"`{message.author.name}#{message.author.discriminator}`")
				embed.add_field(name="Roll", value=f"`{roll}`")
				embed.add_field(name="Result", value=f"`{result}`")
				await message.channel.send(embed=embed)
			
			# info and help command
			elif re.search(rf"{PREFIX}(info|help)", message.content):
				# create embed
				embed = discord.Embed(title="Info", color=BLUE)
				embed.set_thumbnail(url=str(client.user.avatar_url))
				embed.add_field(name="Usage", value=f"`{PREFIX}roll [count]d[faces]*[factor]`", inline=False)
				embed.add_field(name="GitHub", value=r"https://github.com/InformaticFreak/QuantumDice", inline=False)
				embed.add_field(name="Invite", value=INVITE, inline=False)
				await message.channel.send(embed=embed)

# run
client = MyClient()
client.run(TOKEN)
