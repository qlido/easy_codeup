import webbrowser
import keyboard

# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# webbrowser.open('http://docs.python.org/')
NL = int(input("지금 풀고있는 단계를 입력 : "))
# f = open("C:\\st.txt", 'w')
# f.write(str(NL))
# f.close()
url = r"https://codeup.kr/problem.php?id="
webbrowser.open(url + str(NL))
while True:
    if keyboard.read_key() == "1" and keyboard.read_key() == "3":
        NL = NL + 1
        webbrowser.open(url + str(NL))

    if keyboard.read_key() == "2" and keyboard.read_key() == "4":
        break
