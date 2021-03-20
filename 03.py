i = input('Do you have a problem in your life? (yes/no) : ')
x = "Don't worry"
yes = 'yes'
no = 'no'

if i.lower().strip() == yes:

    i = input('Can you do something about it ? (yes/no): ').lower().strip()
    if i == yes:
        print('{}'.format(x))
    if i == no:
        print('{}'.format(x))
else:
    print('{}'.format(x))

# while True:
#     i = input('Do you have a problem in your life? (yes/no): ' )
#     x = "Don't worry"
#     yes = 'yes'
#     no = 'no'

#     if i.lower().strip() == yes:

#         i = input('Can you do someting about it? (yes/no): ').lower().strip()
#         if i == yes:
#             print('{}'.format(x))

#         if i == no:
#             print('{}'.format(x))
#             break
#         else:
#             break
#     else:
#         print('{}'.format(x))
#         break
