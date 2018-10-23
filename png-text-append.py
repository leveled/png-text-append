#!/usr/bin/env python3

import png
import argparse

def insert_text_chunk(png_file,text):

    with open(text,'r') as text_file:
        text_content=text_file.read()

    reader = png.Reader(filename=png_file)
    chunks = reader.chunks()
    chunk_list = list(chunks)
    chunk_item = tuple(['tEXt',bytes(text_content,'utf-8')])
    chunk_list.insert(1, chunk_item) #insert tEXt chunk after iHDr

    with open(png_file,'wb') as dst_file:
        png.write_chunks(dst_file, chunk_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Appends a tEXt section to a png')
    parser.add_argument('png',help='png file') # positional argument with any number of arguments
    parser.add_argument('-t','--text',help='text file to be read and inserted into png tEXt section')
    args = parser.parse_args()

    insert_text_chunk(args.png,args.text)


