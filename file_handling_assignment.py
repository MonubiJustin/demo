try:
    f1=open('my_file.txt', 'w+')
    f1.write('This is line 1\n')
    f1.write('1,2,3,4,5')
    f1.write('\nThis is line 3')
    f1.seek(0)
    print(f1.read())
    f1 = open('my_file.txt', 'a')
    f1.write('\nThis is line 1\n')
    f1.write('1,2,3,4,5')
    f1.write('\nThis is line 3')
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except PermissionError:
    print("Error: Permission denied to access the file 'my_file.txt'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Program execution complete.")

