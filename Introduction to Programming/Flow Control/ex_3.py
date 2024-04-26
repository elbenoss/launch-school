#Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')     # Product2 because case '113' 
bar_code_scanner(142)       # Product not found! because 142 not '142' doesn't have a special case and uses the otherwise case on bottom

