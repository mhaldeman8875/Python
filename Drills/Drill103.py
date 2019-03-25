import sqlite3


fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', \
            'World.txt', 'data.pdf', 'myPhoto.jpg')
fileIndex = len(fileList)

def fileType():
    i = 0
    textFiles = []
    while i < fileIndex:
        if fileList[i].endswith(".txt"):
            textFiles.append(fileList[i])
            i+=1
        else: i+=1
    return textFiles

fileType()

textFiles = fileType()
textIndex = len(textFiles)


conn = sqlite3.connect('Drill_103DB.db')
with conn:

    cur = conn.cursor()
    cur.execute("create table if not exists tbl_files \
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, col_fileList TEXT)")
    for i in range(textIndex):
        cur.execute('INSERT INTO tbl_files(col_fileList) VALUES(?)', [textFiles[i]])
    conn.commit()
conn.close()

for i in textFiles:
    print(i)
            


            

    
        
        
    

