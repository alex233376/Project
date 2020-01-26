from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages = {
'sarah': 'c',
'jen': 'python',
'edward': 'ruby',
'phil': 'C++',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())