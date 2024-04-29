
from discord import Message, Client, PartialEmoji, Member

MESSAGES = {}

async def awen_a(client: Client, user: Member, reaction: PartialEmoji, message: Message, config: dict):
    
    # Check that the react is a STOP
    
    m_id = message.id
    user = user.id
    
    if reaction.name != "🛑":
        return
    
    if m_id not in MESSAGES:
        MESSAGES[m_id] = {
            "votes":   [],
            "message": message
        }
    
    if not user in MESSAGES[m_id]["votes"]:
        MESSAGES[m_id]["votes"].append(user)
        print(f"Delete vote for message {m_id} (votes: {len(MESSAGES[m_id]["votes"])}/{config["STOP_MESSAGE_AMOUNT"]})")
    
    if len(MESSAGES[m_id]["votes"]) >= config["STOP_MESSAGE_AMOUNT"]:
        
        # delete message
        
        print(f"Deleting message {m_id} (votes: {len(MESSAGES[m_id]["votes"])}/{config["STOP_MESSAGE_AMOUNT"]})")
        
        await message.delete()