leftfingers = set("qwertasdfgzxcvb")
rightfingers =set("yuiophjklnm")
group1 = set("tester")
group2 = set("polly")
group3 = set("clarusway")
letfcheck1 = bool(group1.intersection(leftfingers))
rightcheck1 = bool(group1.intersection(rightfingers))
leftcheck2 = bool(group2.intersection(leftfingers))
rightcheck2 = bool(group2.intersection(rightfingers))
leftcheck3 = bool(group3.intersection(leftfingers))
rightcheck3 =bool(group3.intersection(rightfingers))
print(f"tester = {letfcheck1 and rightcheck1}")
print(f"pooly = {leftcheck2 and rightcheck2}")
print(f"clarusway = {leftcheck3 and rightcheck3}")