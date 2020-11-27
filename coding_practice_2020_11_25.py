#34
number = int(input())
if number %2 == 0:
    print("even")
else:
    print("odd")

#35
human_years = int(input)
if human_years == 1 or 2:
    dog_years = 10.5 * human_years
    print(dog_years)
elif human_years > 2:
    dog_years = (10.5 * 2) + (4 * human_years)
    print(dog_years)
elif human_years < 0:
    print(-1)

#36
letter = input()
if letter is "a" or "e" or "i" or "o" or "u":
    print("letter entered is vowel")
elif letter is "y":
    print("y is sometimes a vowel, and sometimes a consonant")
else:
    print("consonant")

#37
sides = int(input);
if sides == 3:
    print("shape is triangle")

elif sides == 4:
    print("shape could be square or rectangle or parallelogram")

elif sides == 5:
    print("shape is pentagon")

elif sides == 6:
    print("shape is hexagon")

elif sides == 7:
    print("shape is heptagon")

elif sides == 8:
    print("shape is octagon")

elif sides == 9:
    print("shape is nonagon")

elif sides == 10:
    print("shape is decagon")

elif sides > 10 or sides < 3:
    print("error")

#38
month = input()
if month in ["january", "march", "may", "july", "august", "october", "december"]:
    print("31 days")

elif month in ["april", "june", "september", "november"]:
    print("30 days")

else:
    print("28 or 29 days")

#39
decibel = int(input)
if decibel == 130:
    print("jackhammer")

elif decibel == 106:
    print("gas lawnmower")

elif decibel == 70:
    print("alarm clock")

elif decibel == 40:
    print("quiet room")

elif decibel < 40:
    print("too quiet")

elif decibel > 130:
    print("too loud")

elif decibel > 40 & decibel <70:
    print("between quiet room and alarm clock")

elif decibel > 70 & decibel < 106:
    print("between alarm clock and lawnmower")

elif decibel >106 & decibel <130:
    print("between gas lawnmower and jackhammer")

#40
first_side = int(input)
second_side = int(input)
third_side = int(input)

if first_side == second_side == third_side:
    print("equilateral")

elif first_side == second_side or first_side == third_side or second_side == third_side:
    print("isosceles")

else:
    print("scalene")

#44
month = int(input)
day = int(input)

if month == 1 & day == 1:
    print("new year's day")

elif month == 7 & day == 1:
    print("canada day")

elif month == 12 & day == 25:
    print("christmas day")

else:
    print("entered month and day do not correspond to a holiday")

#45
position_letter = input()
position_number = int(input)

if position_letter in ["a", "c", "e", "g"] and position_number %2 == 0:
    print("white")

elif position_letter in ["a", "c", "e", "g"] and position_number %2 != 0:
    print("black")

elif position_letter in ["b", "d", "f", "h"] and position_number %2 == 0:
    print("black")

elif position_letter in ["b", "d", "f", "h"] and position_number %2 != 0:
    print("white")

#52
points = float(input)

if points >= 0 & points < 0.5:
    grade = "F"
elif points >= 0.5 & points < 1.15:
	grade = "D"
elif points >= 1.5 & points < 1.5:
	grade = "D+"
elif points >= 1.5 & points < 1.85:
	grade = "C-"
elif points >= 1.85 & points < 2.15:
	grade = "C"
elif points >= 2.15 & points < 2.5:
	grade = "C+"
elif points >= 2.5 & points < 2.85:
	grade = "B-"
elif points >= 2.85 & points < 3.15:
	grade = "B"
elif points >= 3.15 & points < 3.5:
	grade = "B+"
elif points >= 3.5 & points < 3.85:
	grade = "A-"
elif points >= 3.85 & points < 4.0:
	grade = "A"
elif points >= 4.0:
	grade = "A+"
else:
    print("inadmissible points")

print(grade)

def hello_name(name):
  return ("Hello " + name + "!")

def make_abba(a, b):
  return (a+b+b+a)

def make_tags(tag, word):
  return ("<" + tag + ">" + word + "</" + tag + ">")

def make_out_word(out, word):
  return (out[:2] + word + out[2:])

def extra_end(str):
  return (str[-2:]*3)

def first_two(str):
  return (str if len(str)<=2 else str[:2])

def first_half(str):
  return (str[:len(str)/2])

def without_end(str):
  return (str[1:-1])

def combo_string(a, b):
  return (a+b+a if len(a)<len(b) else b+a+b)

def non_start(a, b):
  return (a[1:]+b[1:])
