# Write a program to detect double spaces in a string. 
st = "I m Shivam  i m a good  lad"

# st = input()

doubleSpaces = st.find("  ")

# if(doubleSpaces == -1):
#     print("No double space")
# else:
#     print("double space at", doubleSpaces)

print(doubleSpaces)

#Replace the double spaces from problem 3 with single spaces.

st = st.replace("  ", " ")

print(st)