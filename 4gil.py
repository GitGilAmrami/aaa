try:
    my_file=open("C:\\Users\\user\\Desktop\\DevOps\\4CLASS\\MyFile.txt",'r+')

except IOError:
    print("ERROR")
finally:
    print("RUN ANYWHERE")

# ##my_file=open("C:/Users/user/Desktop/DevOps/4 CLASS/MyFile2.txt",'w+')
#
# #####
# content=my_file.read()
# my_file.write("\ndef")
# print(content)
# my_file.close()
#
# content = my_file.append("\ndef")
# print(content)
# ####
# # my_file=open("C:\\Users\\user\\Desktop\\DevOps\\4 CLASS\\MyFile.txt",'r','encoding=utf-8')


