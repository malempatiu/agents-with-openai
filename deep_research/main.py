from config import check_openai_api_key
from asyncio import run


def do_app_checks():
    check_openai_api_key()


async def main():
    await do_app_checks()
    


if __name__ == '__main__':
    run(main())