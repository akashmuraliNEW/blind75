from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
import asyncio

api_id = 8192282   # Replace with your API ID
api_hash = "990a85e4f02364ddf5927728e75450b5"  # Replace with your API hash
group_id = "@music_mania_Songs"  # Can be @groupname or -1001234567890

app = Client("userbot_session", api_id=api_id, api_hash=api_hash)



async def remove_all_members():
    async with app:
        async for member in app.get_chat_members(group_id):
            user = member.user

            # Skip owners, admins, self, deleted accounts, or bots
            if (
                member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
                or user.is_self
                or user.is_deleted
                or user.is_bot
            ):
                continue

            try:
                await app.ban_chat_member(group_id, user.id)
                await asyncio.sleep(1)
                await app.unban_chat_member(group_id, user.id)
                print(f"Removed: {user.first_name} ({user.id})")
                await asyncio.sleep(5)
            except Exception as e:
                print(f"Failed to remove {user.id}: {e}")
                
asyncio.run(remove_all_members())
