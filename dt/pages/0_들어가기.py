import streamlit as st
import datetime
import pandas as pd
import openai

openai.api_key = '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'

st.set_page_config(layout="wide")

nal = datetime.datetime.now()

if 'userid' not in st.session_state:
    st.error('로그인을 한 후 이용하세요!')
elif st.session_state['userid'] == 'Anonymous':
    st.error('로그인을 한 후 이용하세요!')
    
else:
    st.header('들어가기')
        
    cl1, cl2 = st.columns((15, 9))
    with cl1:
        with st.expander('Content Area'):
            select = st.selectbox('Select Activities Number', ['학습할 내용 선택','떠올려 볼까요?', '무엇을 배울까요?'])
            if select:
                if select =='학습할 내용 선택':
                    pass
                elif select == '떠올려 볼까요?':
                    with open('./data/history.csv', 'a') as f:
                        f.write(f'{st.session_state["userid"]},page0_1,{nal}'+'\n')
                        f.close()
                    st.subheader('떠올려 볼까요?')
                    st.image('./img/원의 중점과 현.png')
                    st.write('한 점 O에서 같은 거리에 있는 점들의 집합으로 이루어진 도형을 무엇이라고 할까요?')
                    st.write('이때 원의 중심과 원 위의 한 점을 이은 것을 무엇이라고 하나요?')
                    st.write('원 위의 두 점을 이은 선분 BC를 원의 무엇이라고 하나요?')
                elif select == '무엇을 배울까요?':
                    with open('./data/history.csv', 'a') as f:
                        f.write(f'{st.session_state["userid"]},page0_2,{nal}'+'\n')
                        f.close()
                    st.subheader('무엇을 배울까요?')
                    st.write('민수가 철수를 부르는 소리는 50m 떨어져 있는 사람한테도 들린다고 한다. 그림의 좌표평면에서 원점 O는 민수의 위치를 점 P(x, y)는 철수의 위치를 나타낸다. 선분 OP의 길이가 50m일 때, x와 y의 관계식을 구해보자')
                    st.image('./img/철수와 민수.png')
            
                else:
                    st.info('error')
            else:
                st.error('학습할 내용을 선택해주세요.')
                
            
    with cl2:
        st.subheader('AI 선생님')
        if 'conversation' not in st.session_state:
            st.session_state['conversation'] = []

        user_input = st.text_input("모르는 것을 질문해보세요!", value="", max_chars=500)
        if st.button('질문하기'):
            if user_input:
                st.session_state['conversation'].append(user_input)
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=st.session_state['conversation'],
                    max_tokens=1500,
                    temperature=0.7
                )
                if 'choices' in response and len(response.choices) > 0:
                    answer = response.choices[0].text.strip()
                    st.session_state['conversation'].append(answer)
                    st.markdown(f"AI 선생님: {answer}")

        if st.button('대화 내용 초기화'):
            st.session_state['conversation'] = []  # Reset conversation history

        with st.expander('대화 내용', expanded=False):
            for i in range(len(st.session_state['conversation'])):
                if st.session_state['conversation'][i].startswith("AI 선생님"):
                    st.markdown(f"<font color='blue'>{st.session_state['conversation'][i]}</font>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<font color='green'>{st.session_state['conversation'][i]}</font>", unsafe_allow_html=True)
