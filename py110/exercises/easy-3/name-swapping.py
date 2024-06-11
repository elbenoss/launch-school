def swap_name(name):
    return name.split()[1] + ', ' + name.split()[0]

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
