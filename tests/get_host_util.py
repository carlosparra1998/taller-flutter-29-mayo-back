def get_host():
        file = open("./host","rb")
        lines=list()
        for line in file.readlines():
                lines.append(line.rstrip().decode("utf-8"))
        file.close()  
        return lines[0]