import sys

file_name = sys.argv[1]

# 読込むファイルのパスを宣言する
# file_name = "./PLG.map"

# 01234567890123456789012345
# RAMDATA SECTION:  000025bc Byte(s)
# ROMDATA SECTION:  000020cf Byte(s)
# PROGRAM SECTION:  00041a4b Byte(s)


try:
    file = open(file_name)
    lines = file.readlines()

    ram =0
    rom =0
    pg  =0

    for line in lines:
        ramstartposi = line.find('RAMDATA SECTION')
        romstartposi = line.find('ROMDATA SECTION')
        pgstartposi  = line.find('PROGRAM SECTION')
        if ramstartposi==0 :
            ramstr = line[ramstartposi+18:ramstartposi+26]
            ram = int(ramstr, 16)
            # print('RAM: ', end="")
            # print(int(ramstr, 16), end="")
            # print(' byte')
        if romstartposi==0 :
            romstr = line[romstartposi+18:romstartposi+26]
            rom = int(romstr, 16)
            # print('ROM: ', end="")
            # print(int(romstr, 16), end="")
            # print(' byte')
        if pgstartposi==0 :
            pgstr = line[pgstartposi+18:pgstartposi+26]
            pg = int(pgstr, 16)
            # print('PROGRAM: ', end="")
            # print(int(pgstr, 16), end="")
            # print(' byte')
except Exception as e:
    print(e)
finally:
    file.close()


    print('-----')
    print('RAM: ', end="")
    print(ram, end="")
    print(' byte')
    print('ROM: ', end="")
    print(rom+pg, end="")
    print(' byte')
    print('-----')

    input('hit any key...')
