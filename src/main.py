from discordbot import bot


if __name__ == "__main__":
    controller = bot.HomeHub(command_prefix="!")
    controller.run_bot()
