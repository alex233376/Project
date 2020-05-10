def make_album(name, album, trek=None):
    full_info = {'executor': name, 'name_album': album}
    if trek:
        full_info['trek'] = trek
    return full_info


info = make_album('petro', 'asd', trek=12)
info1 = make_album('alex', 'faq')
print(f'{info} \n{info1}')
