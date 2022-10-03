import nexo
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("NEXO_PUBLIC_KEY")
secret = os.getenv("NEXO_PUBLIC_KEY")

client = nexo.Client(key, secret)
balances = client.get_account_balances()
print(balances)