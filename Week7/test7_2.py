infile = open("C:\\Dongduk\\4-1summer\\Bigdata\\DONGDUK_4_1_SUMMER\Week7\\dream2.txt", "r")
"""
f = open("파일명", "r,w,a" 중 택1)
f.read: 한 글자씩 읽기
f.readline: 한 줄씩 읽기
f.close() : 파일 닫기
"""
#outfile = open("C:\\Dongduk\\4-1summer\\Bigdata\\DONGDUK_4_1_SUMMER\Week7\\outfile.txt", "w")

#존재 여부 확인
#if os.path.exists("C:\\Dongduk\\4-1summer\\Bigdata\\DONGDUK_4_1_SUMMER\Week7\\dream.txt")
#try문 사용

while 1 :
    contents = infile.readline()
    if not contents :
        break
    print(contents)

word_list = contents.split(" ")
line_list = contents.split("\n")

print("총 글자 수:", len(contents))
print("총 단어 수:", len(word_list))
print("총 줄의 수:", len(line_list))

#outfile.write("총 글자 수:" + str(len(contents)))
#outfile.write("총 단어 수:" + str(len(word_list)))
#outfile.write("총 줄의 수:" + str(len(line_list)))

infile.close()
#outfile.close()
