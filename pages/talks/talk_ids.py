"""
List of talk IDs
"""
import json


schedule_truth = "../../data/speakers-details.json"
schedule_data = json.loads((open(schedule_truth).read()))
TALK_IDS = sorted([x["ID"] for x in schedule_data])
