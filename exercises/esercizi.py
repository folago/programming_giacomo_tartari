x=7
y=3.14
print(x)
print(y)
if x%2==0:
	print("The number is even")
else:
	print("nope")

avrg=(x+y)/2.0
print(avrg)

# 5. change the value of the first variable with its double, subtract 1 to it and 
# put the result into a third variable
z=(x*2)-1
print(z)
# 6. assign values to the four variables x1, y1, x2, y2
# 7. evaluate the euclidean distance for the points (x1,y1) and (x2,y2)
from math import sqrt
x1=4
y1=9
x2=11
y2=7
euclidian_distance =sqrt((x2-x1)**2-(y2-y1)**2)

#     Python-strings

# 1. assign the string “fire and ice” to a variable
s="fire and ice"
# 2. print the third character in the string
# 3. print the fifth character
# 4. print the tenth character, print the last character, print the second to last
print(s[9], s[-1], s[-2]) # The comma is tied to space
print(s[9]+s[-1]+s[-2])
# 5. print the characters in even position
# 6. print the characters in odd position
# 7. print the first half of the string
print(s[:len(s)//2])
# 8. print the whole string in reverse
print(s[::-1])
# 9. count the number of “i” and “e” in the string
print("There are ", s.count("i"), "and ", s.count( "e"), "vovels of the ie class")
# 10. replace the word “and” with “&”
print(s.replace("and", "&"))
# 11. check if the string contains the string “fire”
print("fire" in s)
# 12. check if the string contains the string “re and”
# 13. check if the string contains the string “re &”
# 14. print the position of the first “e
print(s.find("e"))
# 15. print the position of the last “e”
print(  (len(s)-1)  -  (s[::-1].find("i"))   )
print(s[::-1])
print("###################################")
print("lenght of the string: ", len(s))
start = len(s)-1 # index last character
flipped = s[::-1] #so we can count from the right 
print("flipped string: ", flipped)
count_backward = flipped.find("e") # how much we need to count 
print("index of char in flipped: ", count_backward)
result = start - count_backward # we count backward from the last index of the original string
print(result)
print("###################################")


