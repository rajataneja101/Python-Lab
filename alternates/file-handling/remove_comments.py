# 23/02/2017

file_name = input("Enter file name to remove comments from : ")

try:
    f = open(file_name)
except IOError:
    print("Error : file does not exist")
else:
    lines = f.readlines()
    f.close()
    new_file_name = input("Enter new file name : ")
    f = open(new_file_name, "w")

    for line in lines:
        nl = ""
        if(line[0] != "#"):
            for ch in line:
                if(ch == "#"):
                    nl += "\n"
                    break
                nl += ch
            f.write(nl)
    
    print("File updated")