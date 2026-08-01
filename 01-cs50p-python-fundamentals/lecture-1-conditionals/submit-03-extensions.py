# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.


# def last_three(ext):
#     ext = 'cat.gif'
#     return ext[-3]

def main():
    ext = input("What is the file name? ").lower().strip()
    if get_suff(ext) not in ("gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"):
        print("application/octet-stream")
    elif get_suff(ext) in ("gif", "png"):
            print(f"image/{get_suff(ext)}")
    elif get_suff(ext) in ("jpg", "jpeg"):
        print("image/jpeg")
    elif get_suff(ext) == "pdf":
        print(f"application/{get_suff(ext)}")
    elif get_suff(ext) == "txt":
        print("text/plain")
    else:
        print("application/zip")



def get_suff(ext):
    return ext.rsplit(".")[-1]

main()
