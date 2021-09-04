from tkinter import *
import re, numpy
import tkinter.messagebox as msgbox
from matplotlib import pyplot as plt


# RGB 이미지 제작을 위한 배열 제작 함수
def make_rgb_img(sequenceX, img_size):

    codon_1, codon_2 = [], []
  
    for codon in sequenceX:
        if codon == [0]:
            codon_1.append([255,255,255])
        elif codon == ['g','c','t']:
            codon_1.append([127, 5, 47])
        elif codon == ['g','c','c']:
            codon_1.append([255,11,11])
        elif codon == ['g','c','a']:
            codon_1.append([63,2,191])
        elif codon == ['g','c','g']:
            codon_1.append([191,8,191])
        elif codon == ['t','g','t']:
            codon_1.append([23,63,23])
        elif codon == ['t','g','c']:
            codon_1.append([47,127,5])
        elif codon == ['g','a','t']:
            codon_1.append([31,95,11])
        elif codon == ['g','a','c']:
            codon_1.append([63,191,2])
        elif codon == ['g','a','a']:
            codon_1.append([15,47,47])
        elif codon == ['g','a','g']:
            codon_1.append([47,143,47])
        elif codon == ['t','t','t']:
            codon_1.append([15,15,15])
        elif codon == ['t','t','c']:
            codon_1.append([31,31,3])
        elif codon == ['g','g','t']:
            codon_1.append([95,95,35])
        elif codon == ['g','g','c']:
            codon_1.append([191,191,8])
        elif codon == ['g','g','a']:
            codon_1.append([47,47,143])
        elif codon == ['g','g','g']:
            codon_1.append([143,143,143])
        elif codon == ['c','a','t']:
            codon_1.append([1,127,15])
        elif codon == ['c','a','c']:
            codon_1.append([3,255,3])
        elif codon == ['a','t','t']:
            codon_1.append([63,7,7])
        elif codon == ['a','t','c']:
            codon_1.append([127,15,1])
        elif codon == ['a','t','a']:
            codon_1.append([31,3,31])
        elif codon == ['a','a','a']:
            codon_1.append([15,15,15])
        elif codon == ['a','a','g']:
            codon_1.append([47,47,15])
        elif codon == ['c','t','t']:
            codon_1.append([3,31,31])
        elif codon == ['c','t','c']:
            codon_1.append([7,63,7])
        elif codon == ['c','t','a']:
            codon_1.append([1,15,127])
        elif codon == ['c','t','g']:
            codon_1.append([5,47,127])
        elif codon == ['t','t','a']:
            codon_1.append([7,7,63])
        elif codon == ['t','t','g']:
            codon_1.append([23,23,63])
        elif codon == ['a','t','g']:
            codon_1.append([95,11,31])
        elif codon == ['a','a','t']:
            codon_1.append([31,31,3])
        elif codon == ['a','a','c']:
            codon_1.append([63,63,0])
        elif codon == ['c','c','t']:
            codon_1.append([7,7,63])
        elif codon == ['c','c','c']:
            codon_1.append([15,15,15])
        elif codon == ['c','c','a']:
            codon_1.append([3,3,255])
        elif codon == ['c','c','g']:
            codon_1.append([11,11,255])
        elif codon == ['c','a','a']:
            codon_1.append([0,63,63])
        elif codon == ['c','a','g']:
            codon_1.append([2,191,63])
        elif codon == ['c','g','t']:
            codon_1.append([5,127,47])
        elif codon == ['c','g','c']:
            codon_1.append([11,255,11])
        elif codon == ['c','g','a']:
            codon_1.append([2,63,191])
        elif codon == ['c','g','g']:
            codon_1.append([8,191,191])
        elif codon == ['a','g','a']:
            codon_1.append([47,15,47])
        elif codon == ['a','g','g']:
            codon_1.append([143,47,47])
        elif codon == ['t','c','t']:
            codon_1.append([31,3,31])
        elif codon == ['t','c','c']:
            codon_1.append([63,7,7])
        elif codon == ['t','c','a']:
            codon_1.append([15,1,127])
        elif codon == ['t','c','g']:
            codon_1.append([47,5,127])
        elif codon == ['a','g','t']:
            codon_1.append([95,31,11])
        elif codon == ['a','g','c']:
            codon_1.append([191,63,2])
        elif codon == ['a','c','t']:
            codon_1.append([127,1,15])
        elif codon == ['a','c','c']:
            codon_1.append([255,3,3])
        elif codon == ['a','c','a']:
            codon_1.append([63,0,63])
        elif codon == ['a','c','g']:
            codon_1.append([191,2,63])
        elif codon == ['g','t','t']:
            codon_1.append([63,23,23])
        elif codon == ['g','t','c']:
            codon_1.append([127,47,5])
        elif codon == ['g','t','a']:
            codon_1.append([31,11,95])
        elif codon == ['g','t','g']:
            codon_1.append([95,35,95])
        elif codon == ['t','g','g']:
            codon_1.append([35,95,95])
        elif codon == ['t','a','t']:
            codon_1.append([7,63,7])
        elif codon == ['t','a','c']:
            codon_1.append([15,127,1])
        elif codon == ['t','t','a']:
            codon_1.append([7,7,63])
        elif codon == ['t','a','g']:
            codon_1.append([11,95,31])
        elif codon == ['t','g','a']:
            codon_1.append([11,31,95])

        if len(codon_1) == img_size:
            codon_2.append(codon_1)
            codon_1 = []

    Img_x = numpy.array(codon_2)
    # 비교대상1 염기서열 시각화
    plt.imshow(Img_x)
    plt.axis('off')
    plt.savefig("test.png",dpi=3000)
    # plt.show()

# 이미지 크기 결정 함수
def find_size(sequenceX):
    len_seqX = len(sequenceX) # 염기서열 길이 변수에 저장

    # 비교할 두 리스트 중 더 긴 것의 길이를 변수에 저장
    find_size = len_seqX

    # 제곱수 찾기
    for size in range(100001): 
        if size**2 >= find_size :
            img_size=size
            break        

    # 배열의 남은 공간을 0으로 채움
    for i in range(img_size**2):
        if len(sequenceX) < img_size**2:
            sequenceX.append([0])

    # RGB, Colormap 중 선택한 것 실행        
    make_rgb_img(sequenceX, img_size)

# 염기서열 정렬 함수
def sort():
    # 입력받은 염기서열에서 공백과 숫자 제거
    targetX = txt_targetX.get("1.0", END).replace(" ", "").replace("\n", "")
    targetX = re.sub(r'[0-9]+', '', targetX)


    sequenceX= [] # 리스트로 정리된 염기서열

    # 코돈별로 구분해 이중  리스트로 정리
    for i in range(int(len(targetX)/3)):
        targetX_1 = list(targetX[i*3] + targetX[i*3+1] + targetX[i*3+2])
        sequenceX.append(targetX_1)


    find_size(sequenceX) # 이미지 크기 결정 함수 실행

# input창에 염기서열이 입력되었는지 확인
def start():
    if len(txt_targetX.get("1.0", END)) == 1:
        msgbox.showwarning("경고", "염기서열을 입력하세요")
        return # 염기서열을 입력하지 않았으면 경고창 출력
    else:
        sort() # 염기서열을 입력했으면 염기서열 정렬 함수 실행

root = Tk()
root.title("염기서열 시각화")
root.geometry("800x380")
root.resizable(False, False)

# 염기서열 입력 프레임
frame_input = Frame(root, relief="solid", bd=3)
frame_input.pack(fill="both", padx=5, pady=5)

# 비교 대상 1
frame_targetX = LabelFrame(frame_input, text="비교대상1", width=60)
frame_targetX.pack(side="left", fill="both", padx=5, pady=5)

txt_targetX = Text(frame_targetX, width=50, height=15)
txt_targetX.pack(padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

# 시작 버튼
btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.mainloop()