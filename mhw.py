import json
#file = r"C:\Users\Joe\Desktop\Python 3.7 Stuff\armor.json"

with open("armor.json", "r") as gear:
  armour = json.load(gear)



choice = input("Enter your skill name: ")

for armourPiece in armour:
  for skill in armourPiece["skills"]:
    if(skill["skillName"] == choice and armourPiece["rank"] == "high"):
      print("Armour Name: " + armourPiece["name"] + "\n" + "Armour Position: " + armourPiece["type"] + "\n" + "Skill Level: " + str(skill["level"]))
      for slot in armourPiece["slots"]:
        print("Slots Rank: " + str(slot["rank"]))
      print("")