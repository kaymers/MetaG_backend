import os
import sys

if len(sys.argv) >= 2:
    raw_path = sys.argv[1]
    processed_path = sys.argv[2]
    i = 0
    map_file_ptr = open(processed_path, "wb")
    raw_file = open(raw_path)
    for line in raw_file:
        i += 1
        if i == 1:
            continue
        if i % 1000000 == 0:
            print(i, 'records processed')

        asc = line.split()[0]
        tax = int(line.split()[2])
        asc_bytes = asc.encode(encoding='ascii')
        final = asc_bytes + bytes(18-len(asc_bytes)) + tax.to_bytes(4,'little')
        map_file_ptr.write(final)

    map_file_ptr.close()
    raw_file.close()

else :
    print("Argument 1: raw file path\nArgument 2: generated file path")