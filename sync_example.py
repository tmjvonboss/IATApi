from IATApi.Client import SyncClient as Client


def main():
    key = ""
    package = ""
    certificate = ""
    # Initiate client
    client = Client(key=key, package=package, certificate=certificate)
    # Do stuff
    a = client.detect_label("test.jpg")
    print(a["responses"][0])
    # Close client when done
    client.close()


if __name__ == '__main__':
    main()
