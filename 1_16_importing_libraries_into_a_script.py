'''
    modules:modules are the external libraries that you
    can use and include in your project proviving 
    additional functionality without having you write
    that additional functionality 

    for example:regex   i.e:regular expression
'''
#for example
import re
string="'I`M TILAK PARAJULI','i`m 21 years old.','Though we knew it to be true.'"

new=re.sub('[A-Z]','',string)

print(new)
#output:'`  ','i`m 21 years old.','hough we knew it to be true.'

new1=re.sub('[a-z]','',string)
print(new1)

#output: 'I`M TILAK PARAJULI','` 21  .','T      .'

new1=re.sub('[.,\'A-Z +" "]','',string)
print(new1)

string=string+"+977-9864585656"
new2=re.sub('[^0-9]','',string)
print(new2)
