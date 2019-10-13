from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phill'] = 'python'
for name, languages in favorite_languages.items():
    print(name.title() + "'s farite languages is " +
          languages.title() + ".")
