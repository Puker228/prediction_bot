import asyncio

from LxmlSoup import LxmlSoup
from httpx import AsyncClient


async def main():
    # https://horo.mail.ru/prediction/pisces/today/
    # class="rb-p-branding--content rb-p-branding--wrapper"
    async with AsyncClient() as client:
        html = (await client.get("https://horo.mail.ru/prediction/pisces/today/")).text

    soup = LxmlSoup(html)
    d = soup.find_all("main", itemprop="articleBody")
    print(d)


if __name__ == "__main__":
    asyncio.run(main())
