from pyrogram import filters
from pyrogram.types import Message
import base64

ENCODED_REPO = "aHR0cHM6Ly9naXRodWIuY29tL0xlYXJuaW5nQm90c09mZmljaWFsL05vbWFkZUhlbHBCb3Q="


def register_repo_handler(app):

    @app.on_message(filters.command("repo"))
    async def repo_handler(client, message: Message):
        repo_link = base64.b64decode(ENCODED_REPO).decode("utf-8")

        await message.reply_text(
            f"📦 **Official Repository:**\n🔗 {repo_link}",
            disable_web_page_preview=True
        )
