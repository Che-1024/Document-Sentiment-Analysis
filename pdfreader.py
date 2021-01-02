def extract():

    myfile = open("mycv.pdf", "rt") # open lorem.txt for reading text
    contents = myfile.read()         # read the entire file to string
    myfile.close() 
    print(contents)                  # close the file
extract()           # print string contentsS