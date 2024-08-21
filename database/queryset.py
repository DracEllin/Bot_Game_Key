from .models import *
from sqlalchemy import select, delete, update

async def get_categories():
    async with async_session() as session:
        result = await session.scalars(select(Category))
        return result
