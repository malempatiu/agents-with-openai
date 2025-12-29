import asyncio
from agents import Runner, trace
from config import check_openai_api_key
from manager.sales_manager_agent import get_sales_manager_agent


def do_app_checks():
    check_openai_api_key()

async def main():
    do_app_checks()
    message = "Send a cold sales email addressed to Dear CEO from Head of Sales Management"
    with trace("Automated SDR"):
      result = await Runner.run(get_sales_manager_agent(), message)
      print(result)


if __name__ == '__main__':
   asyncio.run(main())
