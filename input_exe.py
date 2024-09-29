def input_exe():

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