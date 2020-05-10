mesto = {}
pooling_active = True

while pooling_active:
    name = input("\nWhat's your name ")
    response = input('Where are you going ')
    mesto[name] = response
    repeat = input('Continue the survey? (eys/no) ')
    if repeat == 'no':
        pooling_active = False
print('\n---Survey result---')
for name, response in mesto.items():
    print(f'{name} would like to go {response}')
