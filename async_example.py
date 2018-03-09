from IATApi.Client import AsyncClient as Client
import asyncio


def main():
    key = ""
    package = ""
    certificate = ""
    loop = asyncio.get_event_loop()
    # Initiate client
    client = Client(key=key, package=package, certificate=certificate)
    # Do your stuff
    a = loop.run_until_complete(client.detect_label("test.jpg"))
    print(a["responses"][0])
    # Close client when done
    loop.run_until_complete(client.close())


if __name__ == '__main__':
    main()
