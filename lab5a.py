#!/usr/bin/env python3
# Author ID: Shazma Hussain - 167689223

def read_file_string(file_name):
    # Reads entire file content and returns it as a string
    with open(file_name, 'r') as f: # Using 'with open' ensures automatic closing
        return f.read()

def read_file_list(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name)) # Prints file as a string
    print(read_file_list(file_name)) # Prints file as a list
