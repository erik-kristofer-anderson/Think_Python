from sec13ex2lib import *

kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')

kanga.put_in_pouch('my item')
kanga.put_in_pouch(roo)


print(kanga)

print(roo)
# print(type(roo))
#
# print(kanga)
# print(roo)
# print(id(roo))
print(id(kanga.pouch_contents))
print(id(roo.pouch_contents))
