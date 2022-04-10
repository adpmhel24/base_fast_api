# import asyncio
# import sys
# import os

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
# import logging


# from app.db.init_super_user import create_initial_su
# from app.db.session import AsyncSessionLocal

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


# async def init():
#     async_session = AsyncSessionLocal

#     async with async_session() as session:
#         await create_initial_su(session=session)


# async def main() -> None:
#     logger.info("Creating initial data")
#     await init()
#     logger.info("Initial data created")


# if __name__ == "__main__":
#     asyncio.run(main())
