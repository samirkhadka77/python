def check_word():
    word = "python"
    with open("practice.txt", "r") as f:
      data = f.read()
    if (data.find(word) != -1):
        print("found")
    else:
        print("not found")

check_word()

