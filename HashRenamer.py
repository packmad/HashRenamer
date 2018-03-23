import hashlib
import os
import sys


def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()


def rename_with_hash(directory):
    i = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = sha256_checksum(file_path)
            os.rename(file_path, os.path.join(root, "{}.apk".format(file_hash)))
            i += 1
    print("{} files renamed".format(i))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main_dir = sys.argv[1]
        if os.path.exists(main_dir):
            if os.path.isdir(main_dir):
                rename_with_hash(main_dir)
            else:
                print("This file '{}' is not a directory".format(main_dir))
        else:
            print("The directory '{}' does not exist".format(main_dir))
    else:
        print("Wrong number of arguments")
