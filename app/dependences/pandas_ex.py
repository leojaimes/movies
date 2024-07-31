import pandas as pd
from pymongo import MongoClient
from app.config import Config


client = MongoClient(Config.MONGO_DB_URI)

db = client["teslo"]
collection = db["products"]
data = list(collection.find())


df = pd.DataFrame(data)


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
