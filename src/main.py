import config, os
from bot import bot

if os.curdir != 'src':
    os.chdir('src')

for i in os.listdir('commands'):
    if i.endswith('.py'):
        name = i.removesuffix('.py')
        print(f'Loading command {name}...')
        bot.load_extension(f'commands.{name}')
        

for i in os.listdir('events'):
    if i.endswith('.py'):
        name = i.removesuffix('.py')
        print(f'Loading event {name}...')
        bot.load_extension(f'events.{i.removesuffix('.py')}')

bot.run(config.TOKEN)