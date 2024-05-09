import asyncio

import discord_bot


async def main():
    # Initialize and run the bot
    await discord_bot.run_bot()

    # Retrieve the collected messages
    messages = discord_bot.get_messages()
    # print(messages)

    seb_list = []
    joey_list = []
    ryan_list = []
    group_streak = False
    seb_streak = False
    joey_streak = False
    ryan_streak = False

    try:
        seb_list.append(messages[496945693408362496])
    except KeyError:
        pass

    try:
        joey_list.append(messages[432018295080878080])
    except KeyError:
        pass

    try:
        ryan_list.append(messages[541887251299303474])
    except KeyError:
        pass

    if (len(seb_list) > 0) and (len(ryan_list) > 0) and (len(joey_list) > 0):
        group_streak = True

    if len(seb_list) > 0:
        seb_streak = True
    if len(joey_list) > 0:
        joey_streak = True
    if len(ryan_list) > 0:
        ryan_streak = True

    return group_streak, seb_streak, joey_streak, ryan_streak


if __name__ == "__main__":
    asyncio.run(main())
