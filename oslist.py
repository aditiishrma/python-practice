import os 
folders = os.listdir("data")

print(folders)
for folder in folders :
    print(folder)
    print(os.listdir(f"data/{folder}"))  # If in some file we had written something then it will also get displayed