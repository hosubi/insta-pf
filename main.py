# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.header('인스타 :red[프로필!]', divider='rainbow')
st.write('프로필!:exclamation:')
       
content = st.text_input('주제, 키워드 입력!  :memo:, !')
prompt = '''As an Instagram pundit, please analyze the profile setting of examples (#topic, keyword) and make a recommended profile example when you provide it!
예시:
섭엗 | 쉬운 마케팅 + 동기부여
망한계정 (3년 방치된 계정)에서
릴스1개 ➡️ 24만뷰+팔로1500명❗️
🎁터지는 제목 생성기! 👇무료전자책🫡
⬇️ 캡션 생성기 ,릴스떡상계산기🚀

[예시 값을 바탕으로 답변!
답변시 예시와 같은 글형식! 줄 맞춤!
(1문장 제목,
2문장 성과,
3문장 혜택제공)
가독성 좋게! 총3~4문장 답변!
예시 참고! 최적의 결과을 만들줘!(결과값만!)
예시 재사용 금지!]
#주제 키워드:'''


if st.button('릴스 프로필!'):
    with st.spinner('시간이 걸릴 수 있어요! 기다려주세요! 추천 중...'):
        result = chat_model.predict( prompt + content )
        st.write(result)

  


st.link_button("토스후원하기, :passenger_ship:", "https://toss.me/aicopy")
st.link_button("buy me a coffee, :coffee:", "https://www.buymeacoffee.com/aicopy")

st.subheader('SNS 추천글!', divider='rainbow') 
st.link_button("광고문의 :coffee:", "https://open.kakao.com/o/s0ic2hMf")
