import asyncio
from datetime import datetime, timedelta

import discord

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

user_messages = {}  # Global dictionary


class DiscordBot(discord.Client):
    async def on_ready(self):
        print("Bot is starting...")
        await self.fetch_messages()
        await self.close()

    async def fetch_messages(self):
        current_time = datetime.now()
        one_day_ago = current_time - timedelta(days=1)
        for channel in self.get_all_channels():
            if isinstance(channel, discord.TextChannel):
                async for message in channel.history(limit=None, after=one_day_ago):
                    if message.author.id in [
                        496945693408362496,
                        432018295080878080,
                        541887251299303474,
                    ]:
                        if message.author.id not in user_messages:
                            user_messages[message.author.id] = []
                        user_messages[message.author.id].append(message.content)
        # print(f"Collected messages: {user_messages}")


async def run_bot():
    bot = DiscordBot(intents=intents)
    try:
        await bot.start(
            "DISCORD_TOKEN"
        )
    finally:
        await bot.close()
        await asyncio.sleep(1)
        print("Bot is closed")


def get_messages():
    return user_messages


if __name__ == "__main__":
    asyncio.run(run_bot())
