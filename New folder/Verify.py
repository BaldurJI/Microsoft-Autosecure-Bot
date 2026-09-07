import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# SENDMSG COMMAND
@bot.command()
async def sendmsg(ctx):

    await ctx.send(
        "📢 What type of message do you want to send?\n\n"
        "Type:\n"
        "`custom` = Send your own message\n"
        "`pvp` = PvP Tournament Message\n"
        "`verify` = Verification Message"
    )

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg_type = await bot.wait_for("message", timeout=60.0, check=check)

        # CUSTOM MESSAGE
        if msg_type.content.lower() == "custom":

            await ctx.send("✍️ Send the custom message now:")

            custom_msg = await bot.wait_for("message", timeout=120.0, check=check)

            await ctx.send(custom_msg.content)

        # PVP MESSAGE
        elif msg_type.content.lower() == "pvp":

            await ctx.send(
                "🚨 **PvP TOURNAMENT ANNOUNCEMENT** 🚨\n\n"
                "⚔️ Ultimate 2v2 PvP Tournament!\n"
                "🏆 Prize Pool: $100 CASH\n"
                "👥 Team Size: 2 Players\n\n"
                "📌 You must verify first to participate.\n"
                "@everyone"
            )

        # VERIFY MESSAGE
        elif msg_type.content.lower() == "verify":

            await ctx.send(
                "**Sorry, It seems You haven't Verified Yet!**\n"
                "To unlock all features and register, verify first."
            )

        else:
            await ctx.send("❌ Invalid option.")

    except:
        await ctx.send("⌛ Time expired.")

bot.run("")
