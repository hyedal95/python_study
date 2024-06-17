from gtts import gTTS
# gtts 라이브러리에서 gTTS만 가져오겠다.

text ="안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS (text = text, lang='ko')
tts.save(r"3.텍스트를 음성으로 변환하기\hi.mp3")
# 폴더 안에 저장하고 싶다. 상대경로 복사
# 앞에 r을 적음으로써 역슬래쉬에는 특별한 기능을 쓰지 않겠다고 지정한다.