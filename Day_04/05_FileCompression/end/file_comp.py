"""
Compress the given file using gzip.
"""

import os
import shutil
import gzip

# Specify input file path and output file path.
input_file_path = '../../04_ExtConversion/end/ext_convert.py'
output_file_path = 'ext_convert.py.gz'

# Open file to be compressed in 'rb' mode and output file in 'wb' mode using
# gzip.open() and use shutil module to copy the data form input file to output
# file.
with open(input_file_path, 'rb') as f_in:
    with gzip.open(output_file_path, 'wb', compresslevel=9) as f_out:
        shutil.copyfileobj(f_in, f_out)


# Check the size of original file and compressed file.
in_size = os.path.getsize(input_file_path)
out_size = os.path.getsize(output_file_path)

print(f"Input file size: {in_size}")
print(f"Output file size: {out_size}")