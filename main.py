print("well come to love calculator")
name1=(input("what is your name?"))
name2=(input("Whaat is their name?"))
name = name1+ name2
#print(f"your name is{name}")
lower_case_name = name.lower()
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

true = t + r + u + e

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

love = l + o + v + e
love_score=int(str(true)+str(love) )
print(love_score)
if love_score<10 or love_score>90:
  print(f"your love score is:{love_score},you go together like coke and mentos")
elif love_score>=40 and love_score<=50:
  print(f"your love score is:{love_score}  ,you are alright together.")
else:
  print(f"your love score is:{love_score}")
