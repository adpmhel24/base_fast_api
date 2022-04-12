from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, text


class CRUDBase:
    async def alter_pk(self, session: AsyncSession, db: Any, sequence: str):
        """
        Example:
            alter_pk(session=session, db=System_Users, sequence="system_users_id_seq")
        """
        statement1 = select(func.max(db.id))
        exec1 = await session.execute(statement1)
        result1 = exec1.scalars().first()
        if not result1:
            result1 = 0

        statement2 = text(
            f"""
        ALTER SEQUENCE {sequence} RESTART {result1+1};
        """
        )
        await session.execute(statement2)
