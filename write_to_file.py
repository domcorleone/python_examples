"""
    Author: Eder Machado
    Description: Write data to a file using python
    Date: 19.102022 11:29 AM
"""

# Declare some variables

writeMe = 'Example text'

saveFile = open('exampleWrite.txt', 'w')
saveFile.write(writeMe)
saveFile.close()
