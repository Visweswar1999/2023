import re

vis = "example for meta char and regular expression"

print("use of star symbol")

res = re.findall("ex{2}",vis)

print(res)

print("use of plus symbol")

res1 = re.findall("ex+",vis)

print(res1)

