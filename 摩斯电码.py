print("摩斯电码互换程序！")
chose = 0
word1 = ""
word2 = ""
lei = ""
while True:
    word1 = ""
    word2 = ""
    lei = ""
    chose = int(input("1、加密 2、解密:"))
    if chose==1:
        word1 = input("请输入需要加密的内容（请不要换行,全部输入小写）：")
        for i in range(len(word1)):
            if word1[i] == 'a':
                word2 = word2+".- "
            elif word1[i] == 'b':
                word2 = word2+"-... "
            elif word1[i] == 'c':
                word2 = word2+"-.-. "
            elif word1[i] == 'd':
                word2 = word2+"-.. "
            elif word1[i] == 'e':
                word2 = word2+". "
            elif word1[i] == 'f':
                word2 = word2+"..-. "
            elif word1[i] == 'g':
                word2 = word2+"--. "
            elif word1[i] == 'h':
                word2 = word2+".... "
            elif word1[i] == 'i':
                word2 = word2+".. "
            elif word1[i] == 'j':
                word2 = word2+".--- "
            elif word1[i] == 'k':
                word2 = word2+"-.- "
            elif word1[i] == 'l':
                word2 = word2+".-.. "
            elif word1[i] == 'm':
                word2 = word2+"-- "
            elif word1[i] == 'n':
                word2 = word2+"-. "
            elif word1[i] == 'o':
                word2 = word2+"--- "
            elif word1[i] == 'p':
                word2 = word2+".--. "
            elif word1[i] == 'q':
                word2 = word2+"--.- "
            elif word1[i] == 'r':
                word2 = word2+".-. "
            elif word1[i] == 's':
                word2 = word2+"... "
            elif word1[i] == 't':
                word2 = word2+"- "
            elif word1[i] == 'u':
                word2 = word2+"..- "
            elif word1[i] == 'v':
                word2 = word2+"...- "
            elif word1[i] == 'w':
                word2 = word2+".-- "
            elif word1[i] == 'x':
                word2 = word2+"-..- "
            elif word1[i] == 'y':
                word2 = word2+"-.-- "
            elif word1[i] == 'z':
                word2 = word2+"--.. "
            elif word1[i] == '1':
                word2 = word2+".---- "
            elif word1[i] == '2':
                word2 = word2+"..--- "
            elif word1[i] == '3':
                word2 = word2+"...-- "
            elif word1[i] == '4':
                word2 = word2+"....- "
            elif word1[i] == '5':
                word2 = word2+"..... "
            elif word1[i] == '6':
                word2 = word2+"-.... "
            elif word1[i] == '7':
                word2 = word2+"--... "
            elif word1[i] == '8':
                word2 = word2+"---.. "
            elif word1[i] == '9':
                word2 = word2+"----. "
            elif word1[i] == '0':
                word2 = word2+"----- "
            elif word1[i] == '.':
                word2 = word2+".-.-.- "
            elif word1[i] == ',':
                word2 = word2+"--..-- "
            else:
                word2 = word2+word1[i]+" "
        word2 = word2
        print("加密后的内容是：{}".format(word2))
    else:
        lei = ""
        word1 = input("请输入需要解密的内容（请不要换行,并在最后添加一个空格）：")
        for i in range(len(word1)):
            if word1[i] == '.':
                lei = lei+"."
            elif word1[i] == '-':
                lei = lei + "-"
            elif word1[i] == ' ':
                try:
                    if lei == ".-":
                        word2 = word2 + 'a'
                    elif lei == "-...":
                        word2 = word2 + 'b'
                    elif lei == "-.-.":
                        word2 = word2 + 'c'
                    elif lei == "-..":
                        word2 = word2 + 'd'
                    elif lei == ".":
                        word2 = word2 + 'e'
                    elif lei == "..-.":
                        word2 = word2 + 'f'
                    elif lei == "--.":
                        word2 = word2 + 'g'
                    elif lei == "....":
                        word2 = word2 + 'h'
                    elif lei == "..":
                        word2 = word2 + 'i'
                    elif lei == ".---":
                        word2 = word2 + 'j'
                    elif lei == "-.-":
                        word2 = word2 + 'k'
                    elif lei  == ".-..":
                        word2 = word2 + 'l'
                    elif lei == "--":
                        word2 = word2 + 'm'
                    elif lei == "-.":
                        word2 = word2 + 'n'
                    elif lei == "---":
                        word2 = word2 + 'o'
                    elif lei == ".--.":
                        word2 = word2 + 'p'
                    elif lei == "--.-":
                        word2 = word2 + 'q'
                    elif lei == ".-.":
                        word2 = word2 + 'r'
                    elif lei == "...":
                        word2 = word2 + 's'
                    elif lei == "-":
                        word2 = word2 + 't'
                    elif lei == "..-":
                        word2 = word2 + 'u'
                    elif lei == "...-":
                        word2 = word2 + 'v'
                    elif lei == ".--":
                        word2 = word2 + 'w'
                    elif lei == "-..-":
                        word2 = word2 + 'x'
                    elif lei == "-.--":
                        word2 = word2 + 'y'
                    elif lei == "--..":
                        word2 = word2 + 'z'
                    elif lei == ".----":
                        word2 = word2 + '1'
                    elif lei == "..---":
                        word2 = word2 + '2'
                    elif lei == "...--":
                        word2 = word2 + '3'
                    elif lei == "....-":
                        word2 = word2 + '4'
                    elif lei == ".....":
                        word2 = word2 + '5'
                    elif lei == "-....":
                        word2 = word2 + '6'
                    elif lei == "--...":
                        word2 = word2 + '7'
                    elif lei == "---..":
                        word2 = word2 + '8'
                    elif lei == "----.":
                        word2 = word2 + '9'
                    elif lei == "-----":
                        word2 = word2 + '0'
                    elif lei == ".-.-.-":
                        word2 = word2 + '.'
                    elif lei == "--..--":
                        word2 = word2 + ','
                    else:
                        word2 = word2 + " "
                    lei=""
                except Exception as e:
                    pass
            else:
                word2 = word2 + word1[i]
        print("解密后的结果为：{}".format(word2))