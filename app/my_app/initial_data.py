import asyncio
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import logging


from .db.session import AsyncSessionLocal
from .db.init_db import create_initial_su

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def init():
    async_session = AsyncSessionLocal

    async with async_session() as session:
        try:
            await create_initial_su(session=session)
        finally:
            await session.close()


async def main() -> None:
    logger.info("Creating initial data")
    await init()
    logger.info("Initial data created")


if __name__ == "__main__":
    asyncio.run(main())
