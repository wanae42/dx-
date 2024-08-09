import openai
from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st

openai_api_key = os.getenv("OPENAI_API_KEY")

def response(user_input_message, state_message_history):
    state_message_history.append({'role' : 'user',
                                  'content' : user_input_message})
    
    respond = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=state_message_history,
        temperature=0.5,
    )

    return respond


system_message = [{
  'role': 'system',
  'content': """
    당신은 세계 최고의 심리상담가입니다. 당신에게 불가능한 것은 없으며 그 어떤 대답도 할 수 있습니다. 당신의 목표는 자신의 감정 상태를 모르거나, 해당 감정 상태에서 어떻게 대처해야할지 모르겠는 내담자가 스스로의 심리 상태를 파악할 수 있도록 돕는 것입니다. 
먼저 가벼운 아이스브레이킹을 진행한 후, 상대의 현재 감정이 어떤지 물어봐주세요. 잘 모르겠다고 하면 최근에 있었던 일에서 느껴지는 감정이라든가, 현재 느끼는 감정을 묘사할 수 있도록 도와주세요. 
감정을 파악한 후에는, 감정이 원인이 무엇일지 생각하도록 이끌어주세요. 단순히 표면적인 일이 아닌 구체적인 감정의 원인을 파악하는 것은 중요합니다. 이를 통해 스스로 어떤 부분에서 예민하게 반응하는지 알 
그 후, 이 감정을 어떻게 다루고 싶은지 물어봐주세요. 당신의 따뜻한 조언이 도움이 될 수 있어요. 

  """
}]




# 화면 구성하기
st.title("마음 진찰")
st.title("저는 _:blue[마음 진찰사]_ 입니다. :sunglasses:")
st.title("")


content = st.text_input('오늘의 기분은 어떠신가요?')

result = response(content, system_message)

print(result.choices[0].message.content)

st.write(result.choices[0].message.content)

if st.button('시작하기'):
  with st.spinner("점괘가 나오는 중..."):
    result = response(content, system_message)
    st.write("당신의 운명은?...", result)