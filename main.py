
# libs
import discord
import re, time, datetime, logging
import secrets, qrng

# globals
PREFIX = r"-"
TOKEN_DC = str(open(r"../TOKEN_DC", "r").readlines()[0].strip("\n"))
TOKEN_IBM = str(open(r"../TOKEN_IBM", "r").readlines()[0].strip("\n"))
INVITE = r"https://discordapp.com/oauth2/authorize?client_id=844685330241159170&permissions=257088&scope=bot"

# colors
BLUE = 0x023059
GOLD = 0xf2c84b

# setup ibm qpc
qrng.set_provider_as_IBMQ(TOKEN_IBM)
qrng.set_backend()

# logging
logging.basicConfig(filename=r"dice_rolls.log", level=logging.INFO, format="%(levelname)s;%(asctime)s;%(message)s", datefmt="%m/%d/%Y;%I:%M:%S")

# client
class MyClient(discord.Client):
	
	# ready
	async def on_ready(self):
		logging.info("ready")
		print("ready")
	
	# recognize command
	async def on_message(self, message):
		if message.author != client.user and message.content.startswith(PREFIX):
			
			# roll command
			if re.search(rf"{PREFIX}q?roll *[0-9]+ *d *[0-9]+ *(\* *[0-9]+)? *", message.content):
				# extract mode
				msg = message.content.replace(" ", "")
				if message.content[len(PREFIX)+1] == "q":
					quantum_mode = True
					msg += f"{message.content[len(PREFIX)+5:]}*1"
				else:
					quantum_mode = False
					msg += f"{message.content[len(PREFIX)+4:]}*1"
				# extract dice data
				count = int(msg.split("d")[0])
				faces = int(msg.split("d")[1].split("*")[0])
				factor = int(msg.split("*")[1])
				# generate dice roll
				if quantum_mode:
					roll = [ round(qrng.get_random_double(1,faces)) for _ in range(count) ]
				else:
					roll = [ secrets.randbelow(faces)+1 for _ in range(count) ]
				# get result
				result = sum(roll) * factor
				# log dice roll
				logging.info("{message};{author};{result};{roll}".format(
					message=message.content.replace("\\", "\\\\"),
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
			
			# info command
			elif re.search(rf"{PREFIX}(info) *", message.content):
				# create embed
				embed = discord.Embed(title="Info", color=BLUE)
				embed.set_thumbnail(url=str(client.user.avatar_url))
				embed.add_field(name="Help", value=f"`{PREFIX}help`", inline=False)
				embed.add_field(name="GitHub", value=r"https://github.com/InformaticFreak/QuantumDice", inline=False)
				embed.add_field(name="Invite", value=INVITE, inline=False)
				await message.channel.send(embed=embed)

			# help command
			elif re.search(rf"{PREFIX}(help) *", message.content):
				# create embed
				embed = discord.Embed(title="Help", color=BLUE)
				embed.set_thumbnail(url=str(client.user.avatar_url))
				embed.add_field(name="Roll Dice", value=f"It rolls `count` times a virtual dice with a certain number of `faces`. The sum of all dice rolls is multiplied by the optional `factor`.\n```{PREFIX}roll [count]d[faces]*[factor]```\nQuantum random numbers are used with `qroll` instead of `roll`.", inline=False)
				embed.add_field(name="Help", value=f"It shows this help.\n```{PREFIX}help```", inline=False)
				embed.add_field(name="Info", value=f"It shows the info.\n```{PREFIX}info```", inline=False)
				await message.channel.send(embed=embed)

# run
client = MyClient()
client.run(TOKEN_DC)
