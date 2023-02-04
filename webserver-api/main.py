import clics
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    token = os.getenv("token")
    user_url = input()

    bitlink = clics.main(token, user_url)
    print(bitlink)
