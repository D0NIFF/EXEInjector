def input_exe(jpeg_path, exe_path, output_path):

    # Read JPEG file
    with open(jpeg_path, 'rb') as jpeg:
        jpeg_content = jpeg.read()

    # Search the marker for end JPEG file
    end_marker = b'\xff\xd9'
    jpeg_end = jpeg_content.find(end_marker) + len(end_marker)

    # Read EXE file
    with open(exe_path, 'rb') as exe:
        exe_content = exe.read()

    # Union JPEG and EXE data
    union_content = jpeg_content[:jpeg_end] + exe_content

    # The record union data in the output file
    with open(output_path, 'wb') as outfile:
        outfile.write(union_content)


jpeg_file = 'image.jpg';    # Path to JPEG file
exe_file = 'program.exe';   # Path to EXE file
output_file = 'image2.jpg'; # Name for the output file

input_exe(jpeg_file, exe_file, output_file)
print(f"EXE inject inside JPEG file. Result: {output_file}")