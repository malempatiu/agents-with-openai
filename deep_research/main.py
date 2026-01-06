from config import check_openai_api_key
from search_agent import search_agent
from asyncio import run


def do_app_checks():
    check_openai_api_key()


async def main():
    await do_app_checks()
    await search_agent()


if __name__ == '__main__':
    run(main())