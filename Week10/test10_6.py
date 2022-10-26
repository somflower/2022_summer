from LAB10_1 import Note
from LAB10_1 import NoteBook

contents = "노트 1페이지 내용"
note1 = Note(contents)#노트에 내용 쓰기
print(note1)
note1.remove()#노트 삭제

contents = "노트 2페이지 내용"
note2 = Note(contents)

contents = "노트 3페이지 내용"
note2 = Note(contents)

ddwu_notebook = NoteBook("파이썬 요약집")
ddwu_notebook.add_note(note2)

print(ddwu_notebook.pages)