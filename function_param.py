"""
    Author: Eder Machado
    Desc: Create functions with parameters
    Date: 18.10.2022 16:14
"""

def addition(num1,num2):
    answer = num1 + num2
    return answer

x = addition(10,30)
print(x)

def website(font,background_color,font_size,font_color):
    print('font:', font)
    print('background_color', background_color)
    print('font_size:',font_size)
    print('font_color:',font_color)

website('Times New Roman','white','11','black')

# The parameters must be inserted in the same order as the original function
# however we can change this order as long as we do like this

print("******************website********************************")
website(font_size='45',
        background_color='white',
        font='Times New Roman',
        font_color='black')

print("*****************website_v2****************************")
# we can define a function with default parameters
# to make easier who calls it and doesn´t want to pass all the values

def website_v2(font='Arial',
               background_color='blue',
               font_size=16,
               font_color='purple'):
    print('font:', font)
    print('background_color:', background_color)
    print('font_size:',font_size)
    print('font_color:',font_color)

# this function will show all default values less the value assigned to the property
# background_color
website_v2(background_color='yellow')
