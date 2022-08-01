from fastapi import APIRouter, HTTPException, Depends

from Schemas import BotUserInDBSchema
from CRUD import CRUDBotUser


bot_user_router = APIRouter(
    prefix="/bot_user"
)


async def check_bot_user_id(bot_user_id: str) -> str | None:
    bot_user = await CRUDBotUser.get(bot_user_id=bot_user_id)
    if bot_user:
        return bot_user_id
    else:
        raise HTTPException(status_code=404, detail="invalid bot_user_id arrived")


@bot_user_router.get("/get", response_model=BotUserInDBSchema, tags=["BotUser"])
async def get_bot_user(bot_user_id: str = Depends(check_bot_user_id)):
    bot_user = await CRUDBotUser.get(bot_user_id=bot_user_id)
    if bot_user:
        return bot_user
    else:
        raise HTTPException(status_code=404, detail="bot_user was not found")


@bot_user_router.get("/all", response_model=list[BotUserInDBSchema], tags=["BotUser"])
async def get_all_bot_user():
    bot_users = await CRUDBotUser.get_all()
    if bot_users:
        return bot_users
    else:
        raise HTTPException(status_code=404, detail="bot_user are not found")


@bot_user_router.post("/add", response_model=BotUserInDBSchema, tags=["BotUser"])
async def add_bot_user(bot_user: BotUserInDBSchema):
    bot_user = await CRUDBotUser.add(bot_user=bot_user)
    if bot_user:
        return bot_user
    else:
        raise HTTPException(status_code=404, detail="this bot_user is exist")


@bot_user_router.delete("/del", tags=["BotUser"])
async def delete_invoice(bot_user_id: str = Depends(check_bot_user_id)):
    await CRUDBotUser.delete(bot_user_id=bot_user_id)
    raise HTTPException(status_code=200, detail=f"bot_user with id {bot_user_id} was deleted")


@bot_user_router.put("/update", tags=["BotUser"])
async def update_bot_user(bot_user: BotUserInDBSchema):
    await CRUDBotUser.update(bot_user=bot_user)
    raise HTTPException(status_code=200, detail="bot_user was updated")
