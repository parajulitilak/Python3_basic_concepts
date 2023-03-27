def printing_something(name,age):
    print("my name is "+name+". \ni`m "+str(age)+" years old.")

printing_something("tilak",21)


#instead of using + we can use comma as
def printing_sth(name1,age1):
    print("\n\n")
    print("hello,name is ",name1,"\ni`m ",age1,"years old.\n\n")

printing_sth("Tilak ",21)


#now let`s create default arguments:
def my_function(name="Someone",age="Unknown"):
    print("my name is ",name,"\ni`m ",age,"years old.\n\n")

my_function("Tilak")

my_function()
