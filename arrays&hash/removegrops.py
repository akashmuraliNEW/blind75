from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
import asyncio

api_id = 123456   # Replace with your API ID
api_hash = "your_api_hash"  # Replace with your API hash
group_username_or_id = "your_group_username_or_id"  # Can be @groupname or -1001234567890

app = Client("userbot_session", api_id=api_id, api_hash=api_hash)

async def remove_all_members():
    async with app:
        async for member in app.get_chat_members(group_username_or_id):
            # Skip admins and self
            if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                continue
            if member.user.is_self:
                continue
            try:
                await app.ban_chat_member(group_username_or_id, member.user.id)
                await app.unban_chat_member(group_username_or_id, member.user.id)
                print(f"Removed {member.user.first_name} ({member.user.id})")
            except Exception as e:
                print(f"Failed to remove {member.user.id}: {e}")

asyncio.run(remove_all_members())
