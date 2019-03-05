import sys
import random

Ver = 'v1.0'
CharKey = '''(q7.бгХюR5p\жТ+$GйiПmЫ’&фKЮНузГЛэпсоLВ*Щ«,6ъцMJ1;ІАtw!l~D<УЧ0bCРкнegzЭ9IОхшr>лч4ФOщfY_Й|'%kЪдUКdЁ[N2XЦ"aрҐ/ЗAVяДP#]W:їj ^Иu?БЄyS)vавBQЕc=тH»n3єёыЯШЖhімoь8T{ZF-}ЇЬґеСМ`xиs@E'''

if len(sys.argv) < 3:

    print()
    print('     FakeFile ' + Ver + ' by MasterDevX')
    print()
    print('     Usage:')
    print('     FakeFile.py FileName FileSize')
    print()
    print('     FileName - Name and extention (if needed) of the output file.')
    print('                Examples: file, program.exe, project.veg, movie.mp4...')
    print()
    print('     FileSize - Size of output file in bytes.')
    print('                Examples: 128, 8192, 45000...')
    print()
    sys.exit()

CharList = [i for i in CharKey]
FileName = str(sys.argv[1])
FileSize = int(sys.argv[2])
File = open (FileName, 'a')

print('[FakeFile] Generating ' + FileName + ', ' + str(FileSize) + ' bytes...')

for i in range(FileSize):
    File.write(CharList[random.randint(0, (len(CharKey) - 1))])
File.close()
