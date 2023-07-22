import streamlit as st
import datetime
import pandas as pd
import openai


openai.api_key = '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'

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

nal = datetime.datetime.now()

if 'userid' not in st.session_state:
    st.error('로그인을 한 후 이용하세요!')
elif st.session_state['userid'] == 'Anonymous':
    st.error('로그인을 한 후 이용하세요!')
else:
    st.header('원의 방정식')
    st.markdown('학습 목표: 원의 방정식을 구할 수 있다.')

    cl1, cl2 = st.columns((15, 9))
    with cl1:
        select = st.selectbox('Select Activities Number', ['학습할 내용 선택','원의 방정식 1', '원의 방정식 2'])
        if select:
            if select =='학습할 내용 선택':
                pass
            elif select == '원의 방정식 1':
                with open('./data/history.csv', 'a') as f:
                    f.write(f'{st.session_state["userid"]},page1_1,{nal}'+'\n')
                    f.close()
                st.subheader('원의 방정식은 어떻게 구할까?')
                st.markdown('좌표평면 위의 한 점 C(a, b)를 중심으로 하고 반지름의 길이가 r인 원을 나타내는 방정식을 알아보자.')
                st.markdown('이 원 위의 임의의 점을 P(x, y)라고 하면 CP=r이므로')
                col3, mid, col4 = st.columns([20,1,20])
                with col3:
                    st.markdown(r"$\sqrt{(x-a)^2+(y-a)^2}= r$")
                    st.markdown('이다. 이 식의 양변을 제곱하면')
                    st.markdown(r"$(x-a)^2+(y-b)^2=r^2$"'······· ㉠')
                with col4:
                    st.image('./img/원의 방정식.png')
                st.markdown('이다. 한편, 점 P(x, y)가 ㉠을 만족시키면 선분CP의 길이는 r이므로 점 P(x, y)는 중심이 C(a,b)이고 반지름의 길이가 r인 원 위의 점이다.')
                st.markdown('따라서 ㉠을 점 C(a, b)를 중심으로 하고 반지름의 길이가 r인 원의 방정식이라고한다.')
                st.markdown('앞의 내용을 정리하면 다음과 같다.')
                st.image('./img/원의 방정식 정리.png')
               
                st.divider()
                iframe_code = "<iframe src='https://www.geogebra.org/material/iframe/id/scdgkykv' width='1200px' height='600px' style='border:0px;'></iframe>"
                st.markdown(iframe_code, unsafe_allow_html=True)   
                st.divider()
                st.subheader('확인문제')             
                st.markdown('확인문제 1. 아래의 원의 방정식을 보고 빈칸에 들어갈 알맞은 단어를 고르시오.')
                st.latex(r'''\sqrt{(x-a)^2+(y-b)^2}=r''')
                ansa1 = st.radio('(1) a의 값이 커지면 좌표평면의 원은 (     ) 으로 이동한다', ['','(1) 왼쪽', '(2) 오른쪽'])
                if ansa1 == '(2) 오른쪽':
                    st.success('정답입니다.')
                else:
                    st.error('오답입니다. 다시 생각해보세요.')
                ansa2 = st.radio('(2) b의 값이 커지면 좌표평면의 원은 (     ) 으로 이동한다', ['','(1) 위쪽', '(2) 아래쪽'])
                if ansa2 == '(1) 위쪽':
                    st.success('정답입니다.')
                else:
                    st.error('오답입니다. 다시 생각해보세요.')
                ansa3 = st.radio('(1) r의 값이 커지면 좌표평면의 원의 크기는', ['','(1) 커진다', '(2) 작아진다'])
                if ansa3 == '(1) 커진다':
                    st.success('정답입니다.')
                else:
                    st.error('오답입니다. 다시 생각해보세요.')
                                
            elif select == '원의 방정식 2':
                with open('./data/history.csv', 'a') as f:
                    f.write(f'{st.session_state["userid"]},page1_2,{nal}'+'\n')
                    f.close()
                st.markdown('이번 장에서는 앞의 장에서 만들었던 원의 방정식을 전개하여 일반형을 만들어 보고자 한다.')
                st.markdown(r"$(x-a)^2+(y-b)^2=r^2$"'를 전개하여 모든 항을 좌변으로 몰아주면 ')
                st.markdown(r"$x^2+y^2-2ax-2yx+a^2+b^2=0$"'이와 같은 원의 방정식의 일반형을 구할 수 있다.')
                st.markdown('이때 'r"$-2a=A,  -2b=B,  a^2+b^2=C$")
                st.markdown('라고 한다면 이 원의 방정식은')
                st.markdown(r"$x^2+y^2+Ax+By+C=0$")
                st.markdown('꼴로 나타낼 수 있다.')
                st.markdown('또한, 위의 x,y에 대한 이차방정식은')
                st.markdown(r"$(x+\frac{A}{2})^2+(y+\frac{B}{2})^2=\frac{A^2+B^2+C}{4}$")
                st.markdown('로 변형할 수 있다. 이때'r"$A^2+B^2-4C>0$"'이면')
                st.markdown('중심이 점'r"$(-\frac{A}{2},-\frac{B}{2})$"'이고')
                st.markdown('반지름의 길이가 'r"$\frac{\sqrt{A^2+B^2-4C}}{2}$"'인 원을 나타낸다.')
                st.markdown('')
                st.markdown('')
                st.markdown('')
                st.markdown('')
                st.divider()
                iframe_code2 = "<iframe src='https://www.geogebra.org/material/iframe/id/kvhff5j3/width/800/height/400/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false' width='800px' height='400px' style='border:0px;'></iframe>"
                st.markdown(iframe_code2, unsafe_allow_html=True)   
                st.divider()
                st.subheader('확인문제')
                st.markdown('원의 방정식 'r"$x^2+y^2-8x-10y-19=0$"' 에 대하여 물음에 답하시오')
                check_pb1 =st.text_input('위의 원의 방정식에서 중점 P를 구하시오')
                if check_pb1 == 'P(4,5)':
                    st.success('정답입니다.')
                else:
                    st.error('오답입니다. 다시 생각해보세요.')
                check_pb2 =st.text_input('위의 원의 방정식에서 반지름의 길이를 구하시오')
                if check_pb2 == '8':
                    st.success('정답입니다.')
                else:
                    st.error('오답입니다. 다시 생각해보세요.')
                st.markdown('')
                st.markdown('')
                st.markdown('')
                st.markdown('')
                st.markdown('')
            
            else:
                st.error('학습내용을 선택해주세요')
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
