
# libs
import discord
import re, os
import qrng, secrets

# globals
PREFIX = r"-"
TOKEN_DC = open(os.path.abspath(r"../TOKEN_DC"), "r").readlines()[0].strip()
TOKEN_IBM = open(os.path.abspath(r"../TOKEN_IBM"), "r").readlines()[0].strip()
INVITE = r"https://discordapp.com/oauth2/authorize?client_id=844685330241159170&permissions=257088&scope=bot"

# colors
BLUE = 0x023059
GOLD = 0xf2c84b

# setup ibm qpc
qrng.set_provider_as_IBMQ(TOKEN_IBM)
qrng.set_backend()

# client
class MyClient(discord.Client):
	
	# ready
	async def on_ready(self):
		print("ready")
	
	# recognize command
	async def on_message(self, message):
		if not message.author is client.user and message.content.startswith(PREFIX):
			
			# roll command
			if re.search(rf"{PREFIX}q?roll [0-9]+d[0-9]+(\*[0-9]+)?( (min|max|normal)?)? *", message.content):
				msg = message.content.split()
				# extract quantum mode
				mode_quantum = False
				if msg[0][len(PREFIX)] == "q":
					mode_quantum = True
				# extract dice data
				msg[1] += "*1"
				count = int(msg[1].split("d")[0])
				faces = int(msg[1].split("d")[1].split("*")[0])
				factor = int(msg[1].split("*")[1])
				# extract min/max mode
				msg.append("normal")
				mode_min_max = str(msg[2])
				# generate dice roll
				if mode_quantum:
					roll = [ round(qrng.get_random_double(1,faces)) for _ in range(count) ]
				else:
					roll = [ secrets.randbelow(faces)+1 for _ in range(count) ]
				# get result
				result = sum(roll) * factor
				# create embed
				if mode_quantum:
					embed = discord.Embed(title="Quantum Iacta Est", color=GOLD)
				else:
					embed = discord.Embed(title="Alea Iacta Est", color=BLUE)
				embed.add_field(name="User", value=f"`{message.author.name}#{message.author.discriminator}`")
				if mode_min_max == "min":
					embed.add_field(name="Min Roll", value=f"`{min(roll)}`")
					result = min(roll) * factor
				elif mode_min_max == "max":
					embed.add_field(name="Max Roll", value=f"`{max(roll)}`")
					result = max(roll) * factor
				else:
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
				embed.add_field(name="Roll Dice", value=f"It rolls `count` times a virtual dice with a certain number of `faces`. The sum of all dice rolls is multiplied by the optional `factor`. The optional `mode` can be *min* or *max*. The mode *min* returns only the lowest roll and *max* only the highest roll.\n```{PREFIX}roll [count]d[faces]*[factor] [mode]```\nQuantum random numbers are used with `qroll` instead of `roll`.", inline=False)
				embed.add_field(name="Help", value=f"It shows this help.\n```{PREFIX}help```", inline=False)
				embed.add_field(name="Info", value=f"It shows the info.\n```{PREFIX}info```", inline=False)
				await message.channel.send(embed=embed)

# run
client = MyClient()
client.run(TOKEN_DC)
