import random
import time
import winsound

## 노래 가사 리스트
            
sentences = []

sentences= ['사랑해 또 사랑해 더 지독하게 아프고 싶어',
'이 밤은 짧고 넌 당연하지 않아',
'넌 날 반쯤 미치게 만들어',
'내 옆에 너 꼭 붙어 있어 봐',
'미쳐가 너와 눈이 마주친 순간',
'색안경을 끼고 보지 마요 난 좀 다른 여자인데',
'소리를 지르는 내가 창빈이란다 내 자리는 내가 취한다',
'미래의 미래에도 널 사랑할 나란 걸',
'처음 느낀 심장의 속도가 이리 빠른 줄 몰랐어',
'널 알아가면 갈수록 내 취향과 패턴 그 모든 게 바뀌어',
'거울 속의 나는 네가 아닐까? 일그러져버린 환영인 걸까?',
'절대적 룰을 지켜 내 손을 놓지 말아',
'나를 무너뜨리고 싶은 네 환각들이 점점 너를 구축할 이유가 돼',
'우린 스케이트보드 위로 마치 춤을 추듯 발을 굴러',
'누가 뭐라해도 난 나야 난 그냥 내가 되고 싶어',
'이대로 지나치지 마요 너도 나처럼 날 잊을 수가 없다면',
'우린 참 별나고 이상한 사이야',
'잊지마 넌 흐린 어둠 사이 왼손으로 그린 별 하나',
'머리는 엉망인 데다 상태가 말이 아니야',
'외로운 날들이여 모두 다 안녕']



## 정답/오답 소리 재생 함수

scale = {'1':200,'2':300,'3':500,'4':600,
         '5':261,'6':329,'7':391,'8':349,'9':293}

def soundplay():
    
    mel1 = ['3','4']
    dur1 = [1,1]

    mel2 = ['2','1']
    dur2 = [1,1]

    sound_correct = zip(mel1,dur1)
    sound_fail = zip(mel2,dur2)


    if question == answer:
        for melody,duration in sound_correct:
            winsound.Beep(scale[melody],200//duration)
    else:
        for melody,duration in sound_fail:
            winsound.Beep(scale[melody],200//duration)


            
## 합격/불합격 소리 재생 함수

def soundplay_2():
    mel3 = ['5','6','7','3']
    dur3 = [1,1,1,1]

    mel4 = ['8','6','9','5']
    dur4 = [1,1,1,1]

    sound_result_c = zip(mel3,dur3)
    sound_result_f = zip(mel4,dur4)
    
    if correct >= 6 and timer < 180:
        for melody,duration in sound_result_c:
            winsound.Beep(scale[melody],200//duration)
    else:
        for melody,duration in sound_result_f:
            winsound.Beep(scale[melody],200//duration)




## 게임 시작 코드

### 언어 설정 코드

language = int(input("*** 시작 언어 설정을 합니다. \n한국어는 1번, 영어는 2번을 입력하고 엔터키를 누르세요. \n\n*** set starting language. \nif you want to set Korean press 1, English 2 and press enter."))
if language == 1:
    input("\n\n[K-POP 타이핑 게임] 엔터키를 누르면 시작합니다")
    print()
    start = time.time()
     
    correct = 0
     
    for i in range(10):
        random.shuffle(sentences)
        question = random.choice(sentences)
        print(f'문제{i+1}) {question}')
        answer = input('>>>>>> ')

   
        if question == answer:
            print('>>>>>> 정답')
            correct += 1
            soundplay()
        

        else:
            print('>>>>>> 오답')
            soundplay()
        
        print()

    end = time.time()
    timer = end - start

    print('=' * 30)

    print(f'게임시간: {timer:.1f}초, 정답: {correct}개')

    if correct >= 6 and timer < 180 :
        print('!!!"합격"!!!')
        soundplay_2()
    
    else:
        print('"불합격"ㅠㅠ')
        soundplay_2()

else :
    input("\n\n[K-POP TYPING GAME] to start press enter")
    print()
    start = time.time()
     
    correct = 0
     
    for i in range(10):
        random.shuffle(sentences)
        question = random.choice(sentences)
        print(f'LYRICS{i+1}) {question}')
        answer = input('>>>>>>>> ')

   
        if question == answer:
            print('>>>>>>>> CORRECT')
            correct += 1
            soundplay()
        

        else:
            print('>>>>>>>> WRONG')
            soundplay()
        
        print()

    end = time.time()
    timer = end - start

    print('=' * 30)

    print(f'PLAY TIME: {timer:.1f} Sec, CORRECT ANSWER: {correct}')

    if correct >= 6 and timer < 180 :
     print('!!!"SUCCESS"!!!')
     soundplay_2()
    
    else:
     print('"FAILED"TOT')
     soundplay_2()

