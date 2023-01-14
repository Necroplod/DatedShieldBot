import discord
import config
from discord import Intents
from discord.ext import commands

class Setup(commands.Bot):
	def main(self):	
		self.remove_command('help')
		self.line = '----------------------------------------------'

		self.EXTENSIONS = [
			'cogs.dev',
			'cogs.suggest'
		]
		self.HANDLERS = [
			'cogs.event'
		]
	
	async def setup_hook(self):
		self.main()
		for extension in self.EXTENSIONS:
			try:
				await self.load_extension(extension)
			except Exception as e:
				print(f'{self.line}\n[!] Не удалось загрузить модуль {extension}.')
				print(f'[!] {e}\n{self.line}')
			else:
				print(f'[!] Модуль {extension} успешно загружен.')
		print(self.line)
		for handler in self.HANDLERS:
			try:
				await self.load_extension(handler)
			except Exception as e:
				print(f'{self.line}\n[!] Не удалось загрузить хендлер {handler}.')
				print(f'[!] {e}\n{self.line}')
			else:
				print(f'[!] Хендлер {handler} успешно загружен.')


client = Setup(
	status = discord.Status.idle,
	case_insensitive = True,
	activity = discord.Streaming(name=f'g.help', url='https://youtu.be/dQw4w9WgXcQ'),
	command_prefix = config.PREFIX, 
	intents = Intents.all())
client.run(config.TOKEN)