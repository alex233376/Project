num = {'alex': [7, 8, 10],
       'nata': [3, 4, 3],
       'vasia': [5, 9, 11],
       'petro': [8, 12, 45],
       'ira': [4, 2, 78]}
for name, nums in num.items():
    print(f"{name.title()}")
    for n in nums:
        print(n)
