import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os


# load enviroment variables from .env file
load_dotenv()

# read MONGO_DB_URI environment var
mongo_uri = os.getenv("MONGO_DB_URI")


client = MongoClient(mongo_uri)

db = client["teslo"]
collection = db["products"]
data = list(collection.find())


df = pd.DataFrame(data)

print(df)


# dataFrame = pd.read_csv("meaningful_output.csv", index_col="id")

# # df_filtred = df.dropna() Delete rows with NaN values in any cell
# # df_filtred.head()

# dataFrame.fillna(
#     value=0
# )  # It is necessary to receive a value; otherwise, an error will be shown.
# print(dataFrame)

# dataFrame.fillna(
#     {"retweets": 0, "followers": 0}
# )  # "This instruction changes NaN values in the column 'retweets' to zero, and zeros in the column 'followers
