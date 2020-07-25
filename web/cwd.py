# import the os module
import os

# detect the current working directory and print it
path = os.getcwd()
print ("The current working directory is %s" % path)
os.mkdir(path+"/gatos_imgs/2")