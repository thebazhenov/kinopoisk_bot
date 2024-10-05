from sqlalchemy import select, delete, Select
from database.models import Users


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(Users).where(Users.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()