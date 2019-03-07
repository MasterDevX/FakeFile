import sys

Ver = 'v1.1'

def usage():

    print()
    print('FakeFile ' + Ver + ' by MasterDevX')
    print()
    print('Usage:')
    print('FakeFile.py FileName FileSize SizeUnit')
    print()
    print('FileName - Name and extention (if needed) of the output file.')
    print('           Examples: file, program.exe, project.veg, movie.mp4...')
    print()
    print('FileSize - Size of output file.')
    print('           Examples: 4, 128, 4000, 8192...')
    print()
    print('SizeUnit - Unit, in which file size is specified:')
    print('           B - Bytes, K - Kilobytes, M - Megabytes, G - Gigabytes.')
    print()
    sys.exit()

try:

    FileName = str(sys.argv[1])
    FileSize = float(sys.argv[2])
    SizeUnit = str(sys.argv[3])
    File = open(FileName, 'wb')

except:

    usage()

if SizeUnit == 'B':

    FileSize = round(float(FileSize))

elif SizeUnit == 'K':

    FileSize = round(float(FileSize * 1024))

elif SizeUnit == 'M':

    FileSize = round(float(FileSize * (1024 ** 2)))

elif SizeUnit == 'G':

    FileSize = round(float(FileSize * (1024 ** 3)))

else:

    usage()

print('[FakeFile] Generating ' + FileName + ', ' + str(FileSize) + ' bytes...')
File.write(b'\0' * FileSize)
print('[FakeFile] File created!')

File.close()
sys.exit()
