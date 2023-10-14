# import os

# API_TOKEN = os.environ.get("API_TOKEN")
# if API_TOKEN is None:
#     raise ValueError("API_TOKEN is not set")
# BOOLEAN_FLAG = os.environ.get("BOOLEAN_FLAG")
# if BOOLEAN_FLAG is None:
#     raise ValueError("BOOLEAN_FLAG is not set")

# if BOOLEAN_FLAG.lower() == "true":
#     BOOLEAN_FLAG = True  # type: ignore
# elif BOOLEAN_FLAG.lower() == "false":
#     BOOLEAN_FLAG = False  # type: ignore
# else:
#     raise ValueError("BOOLEAN_FLAG is not set to True or False")

# if __name__ == "__main__":
#     print(API_TOKEN)
#     print(BOOLEAN_FLAG)

import os

from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    API_TOKEN = os.environ.get("API_TOKEN")
    if API_TOKEN is None:
        raise ValueError("API_TOKEN is not set")
    print(API_TOKEN)
