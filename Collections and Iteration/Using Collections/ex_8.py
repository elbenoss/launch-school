#Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

'''
the f in fjord is located at the 29th position 
text[21:35] slices to start finding at location 21 then finds it 8 later at 29
'''
