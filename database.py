import pymongo
import json
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_CLIENT = os.getenv("MONGO_CLIENT")

client = pymongo.MongoClient(MONGO_CLIENT)

db = client.get_database("osu")

col = db.get_collection("tayuno_quals_result")

quals_result = {}
with open("final_team_score.json", "r") as f:
    quals_result = json.load(f)
f.close()

team_list = list(quals_result.keys())

time_start = datetime.datetime.now()

# for i in range(len(team_list)):
#     d = {"_id": i,
#         team_list[i]: quals_result[team_list[i]]}
#     col.insert_one(d)

time_end = datetime.datetime.now()

print(time_end - time_start)

col = db.get_collection("tayuno_quals_pool")

quals_pool = {}
with open("quals_pool.json") as f:
    quals_pool = json.load(f)
f.close()

quals_id = list(quals_pool.keys())

time_start = datetime.datetime.now()

for i in range(len(quals_id)):
    d = {"_id": i,
        quals_id[i]: quals_pool[quals_id[i]]}
    col.insert_one(d)

time_end = datetime.datetime.now()

print(time_end - time_start)
