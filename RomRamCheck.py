# 読込むファイルのパスを宣言する
file_name = "./data.txt"

try:
    file = open(file_name)
    lines = file.readlines()
    for line in lines:
        romstartposi = line.find('ROMDATA')
        ramstartposi = line.find('RAMDATA')
        if romstartposi==0 :
            romstr = line[romstartposi+8:]
            print(int(romstr, 16), end="")
            print(' byte')
        if ramstartposi==0 :
            ramstr = line[ramstartposi+8:]
            print(int(ramstr, 16), end="")
            print(' byte')
except Exception as e:
    print(e)
finally:
    file.close()
