# STRING FORMATTING can be done using two methods, String Formatting Mecahnism introduced  by PEP 498
  # 1. "Format" method (Traditional Method)

letter="Hey! My name is {} and I belong to {}. I am currently pursuing my degree in {}"
name="Aditi Sharma"
country="India"
course="Btech CSE"
print(letter.format(name,course,country)) # Here order changes, that will lead to wrong output
    # This can be resolved as
sentence="Life is all about{1}, if you escape {1}, you will left with {2}. Its better to focus on your {0} and to build up your {3}"
value1="career"
value2="struggle"
value3="nothing"
value4="strengths"
print(sentence.format(value1,value2,value3,value4))

     #2. "fstring" method
     # It allows you to place variables conveniently inside the string, feature prsent in Python 3.6 version
     
print(f"Hey! My name is {{name}} and I belong to {country}. I am currently pursuing my degree in {course}")     
# txt="For only {price:.2f} dollars!"
# print(txt.format(price=45.233322)) # Using Format method
price=45.233332
txt=f"For only {price:.2f} dollars!"
print(txt)
print(type(f"{7*12}"))