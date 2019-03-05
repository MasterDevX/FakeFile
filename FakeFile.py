import sys

Ver = 'v1.0'

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

FileName = str(sys.argv[1])
FileSize = int(sys.argv[2])
File = open (FileName, 'wb')

print('[FakeFile] Generating ' + FileName + ', ' + str(FileSize) + ' bytes...')
File.write(b'\0' * FileSize)
print('[FakeFile] File created!')
File.close()
sys.exit()
