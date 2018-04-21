{{if AsyncIO}}
import asyncio


async def main():
    pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

{{else}}

def main():
    pass


if __name__ == '__main__':
    main()

{{end}}

