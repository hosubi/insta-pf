# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.header('인스타 :red[프로필!]', divider='rainbow')
st.write('프로필!:exclamation:')
       
content = st.text_input('주제, 키워드 입력!  :memo:, (양식 : 육아 전문가, 아들3명, 건강레시피)와 같이 입력! !')
prompt = '''As an Instagram expert, please analyze the profile setting of the example (#topic, keyword) and make an example of a recommended profile when you provide it! (Readability in the form of text like the example, please protect it!)

Emojis that fit the topic,
A simple sentence with a key point,
Form as in the example,

Example Note! Make the best result! (Result value only!)
[Example: Don't reuse it!]

((예시:
섭엗 | 쉬운 마케팅 + 동기부여
망한계정 (3년 방치된 계정)에서
릴스1개 ➡️ 24만뷰+팔로1500명❗️
🎁터지는 제목 생성기! 👇무료전자책🫡
⬇️ 캡션 생성기 ,릴스떡상계산기🚀))

반드시, 
위 내용의 형식으로 주제에 대한 결과값으로 답변만 부탁해!!
(이모티콘 + 짧은글 + 줄바꿈 + 가독성 좋게!)

#주제 키워드:'''


if st.button('릴스 프로필!'):
    with st.spinner('시간이 걸릴 수 있어요! 기다려주세요! 추천 중...'):
        result = chat_model.predict( prompt + content )
        st.write(result)

  


st.link_button("토스후원하기, :passenger_ship:", "https://toss.me/aicopy")
st.link_button("buy me a coffee, :coffee:", "https://www.buymeacoffee.com/aicopy")

st.subheader('SNS 추천글!', divider='rainbow') 
st.link_button("광고문의 :coffee:", "https://open.kakao.com/o/s0ic2hMf")
