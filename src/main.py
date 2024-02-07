from dotenv import dotenv_values
import hikari
import lightbulb

# Get the env variable and initial bot

env = dotenv_values(".env")

app = lightbulb.BotApp(env["TOKEN"], env["PREFIX"], help_class=None, intents=hikari.Intents.ALL)



# Help command

@app.command()
@lightbulb.command("help", "Help command Specs from github idea")
@lightbulb.implements(lightbulb.PrefixCommand)
async def help(ctx: lightbulb.Context):
    embed = hikari.Embed(title="Regras da batalha naval", description=" - Os jogadores devem determinar a quantidade de cada tipo de navios que irão utilizar. Com isso o jogadore que posiciona os navios podem colocar apenas 4 navios e um de cada tipo\nHá 4 tipos de navios**\nPorta-aviões ocupam 5 espaços\nCruzador ocupam 4 espaços\nContratorpedeiro ocupam 3 espaços\nRebocador ocupam 2 espaços**", color=0x0000ff)
    await ctx.respond(embed=embed)
# Start command

@app.command()
@lightbulb.command("start", "Start the battle Specs from github idea")
@lightbulb.implements(lightbulb.PrefixCommand)
async def start(ctx: lightbulb.Context):
    await ctx.respond("Start command")


# Surrender command
@app.command()
@lightbulb.command("surrender", "Surrender the battle Optional Specs from github idea")
@lightbulb.implements(lightbulb.PrefixCommand)
async def surrender(ctx: lightbulb.SlashCommand):
    await ctx.respond("Surrender command")

# Stated the bot with rich presence "Digit bbhelp to start"
    
app.run(
    activity= hikari.Activity(name="Digit bbhelp to start", type=hikari.ActivityType.PLAYING)
)
