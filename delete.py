import discord
import datetime
import logging

bot = discord.Client()
token = "NzA4NzE2MzUzNTEwNzAzMjE0.Xrbz9Q.ipVNrtijhh5eNNmCh3EeozuR7Is"

logging.basicConfig(level='INFO')


@bot.event
async def on_message_delete(m):
    a = m.author
    if not a.bot:
        c = m.channel
        t = m.content
        embed = discord.Embed()
        embed.description = t
        embed.colour = discord.Colour.light_grey()
        if m.edited_at is None:
            footer = m.created_at.strftime("%-d %b %a %-I:%M %p")
        else:
            footer = f"{m.created_at.strftime('%-d %b %a %-I:%M %p')}\n{m.edited_at.strftime('%-d %b %a %-I:%M %p')} (edited)"
        embed.set_footer(text=footer)
        if isinstance(c, discord.TextChannel):
            name = a.nick
            if name is None:
                name = a.name
        else:
            name = a.name
        embed.set_author(name=name, icon_url=a.avatar_url)
        try:
            await c.send(embed=embed)
        except discord.errors.HTTPException:
            await c.send(f"**{a.mention}:\n**{t}\n{footer}")


@bot.event
async def on_connect():
    print("They shall not delete!")

bot.run(token, bot=False)
