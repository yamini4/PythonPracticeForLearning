# Ask the user for the file name
#filename = input("Enter the filename (with extension): ")
# filename = "C:\\Users\\Yamini Garudachalam\\OneDrive - Prodian Infotech Private Limited\\Desktop\\FileTransfer.txt"

# try:
#     # Open the file in read mode
#     with open(filename, 'r') as file:
#         content = file.read()  # Read the entire file
#         print("\nFile Contents:\n")
#         print(content)

# except FileNotFoundError:
#     print(f"Error: The file '{filename}' does not exist.")
# except Exception as e:
#     print(f"An error occurred: '{filename}'", e)






import os

filename = "C:\\Users\\Yamini Garudachalam\\OneDrive - Prodian Infotech Private Limited\\Desktop\\FileTransfer.txt"

# Check if the file exists
if os.path.exists(filename):
    try:
        # Open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile Contents:\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print("An error occurred while reading the file:", e)
else:
    print(f"Error: The file '{filename}' does not exist.")
