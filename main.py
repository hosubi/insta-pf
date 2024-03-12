# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.header('블로그 :red[소제목 서론 생성기!]', divider='rainbow')
st.write('지수 상승과 체류시간 상승!:exclamation:')
       
content = st.text_input('주제, 키워드 입력!  :memo:, !')
prompt = '''인스타 전문가로써 답변해줘!
아래 예시는 팔로워가 생기는 릴스 팔로워가 생기는 프로필세팅!
참고해서 답변만 작성해줘!
예시:
섭엗 | 쉬운 마케팅 + 동기부여
망한계정 (3년 방치된 계정)에서
릴스1개 ➡️ 24만뷰+팔로1500명❗️
🎁터지는 제목 생성기! 👇무료전자책🫡
⬇️ 캡션 생성기 ,릴스떡상계산기🚀

캡션을 넣으면!
분석과 최적의 대안을 답해줘!(결과값만!)
#:'''


if st.button('블로그 소제목 서론 생성기!'):
    with st.spinner('시간이 걸릴 수 있어요! 기다려주세요! 추천 중...'):
        result = chat_model.predict( prompt + content )
        st.write(result)

  


st.link_button("토스후원하기, :passenger_ship:", "https://toss.me/aicopy")
st.link_button("buy me a coffee, :coffee:", "https://www.buymeacoffee.com/aicopy")

st.subheader('SNS 추천글!', divider='rainbow') 
st.link_button("광고문의 :coffee:", "https://open.kakao.com/o/s0ic2hMf")
