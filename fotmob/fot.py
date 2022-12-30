from mobfot import MobFot
client = MobFot()
# res = client.get_matches_by_date("20221230")
res = client.get_league(id=87)
table = res['table']
print(f"fotmob???: {table[0]}")

# la liga id: 87
# ['tabs', 'details', 'seostr', 'QAData', 'table', 'transfers', 'news', 'overview', 'stats', 'matches', 'playoff']
