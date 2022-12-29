from mobfot import MobFot
client = MobFot()
# res = client.get_matches_by_date("20221230")
res = client.get_league(id=87)
print(f"fotmob???: {res}")

# la liga id: 87
