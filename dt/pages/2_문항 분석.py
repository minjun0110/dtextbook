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
    st.header('원의 방정식 구하기')
    cl1, cl2 = st.columns((15, 5))
    with cl1:
        with st.expander('Content Area'):
            select = st.selectbox('Select Activities Number', ['학습할 내용 선택','한 점을 중점으로 갖고 한 점을 지나는 원의 방정식', '두 점을 지름의 끝으로 같는 원의 방정식','세 점을 지나는 원의 방정식'])
            if select:
                if select =='학습할 내용 선택':
                    pass
                elif select =='한 점을 중점으로 갖고 한 점을 지나는 원의 방정식':
                    with open('./data/history.csv', 'a') as f:
                        f.write(f'{st.session_state["userid"]},page2_1,{nal}'+'\n')
                        f.close()
                    st.subheader('한 점을 중점으로 갖고 한 점을 지나는 원의 방정식')
                    st.markdown('원의 방정식의 중점을 아는 경우 표준형 원의 방정식')
                    st.markdown(r"$(x-a)^2+(y-b)^2=r^2$"'에서 a와 b의 값을 알 수 있다.')
                    st.markdown('이후 원의 방정식이 지나는 점의 x,y 값을 대입하여 'r"$r^2$"'의 값을 알 수 있다.')
                    st.markdown('')
                    st.markdown('')
                    st.divider()
                    st.subheader('확인문제')
                    st.markdown('점O(1,2)를 원의 중심으로 갖고 점(5,-5)를 지나는 원의 방정식 'r"$(x-a)^2+(y-b)^2=c$"' 에 대하여 물음에 답하시오')
                    st.image('./img/check_pc.png')
                    check_pe1 =st.text_input('a의 값은 얼마인가?')
                    if check_pe1 == '1':
                        st.success('정답입니다.')
                    else:
                        st.error('오답입니다. 다시 생각해보세요.')
                    check_pe2 =st.text_input('b의 값은 얼마인가?')
                    if check_pe2 == '-2':
                        st.success('정답입니다.')
                    else:
                        st.error('오답입니다. 다시 생각해보세요.')
                    check_pe3 =st.text_input('C의 값은 얼마인가?')
                    if check_pe3 == '25':
                        st.success('정답입니다.')
                    else:
                        st.error('오답입니다. 다시 생각해보세요.')

                elif select == '두 점을 지름의 끝으로 같는 원의 방정식':
                    with open('./data/history.csv', 'a') as f:
                        f.write(f'{st.session_state["userid"]},page2_2,{nal}'+'\n')
                        f.close()        
                    st.subheader('두 점을 지름의 끝으로 갖는 원의 방정식')
                    st.markdown('두 점을 지름의 끝으로 갖는 경우, 두 점의 중점이 원의 중심이 된다.')
                    st.markdown('따라서 표준형인 'r"$(x-a)^2+(y-b)^2=r^2$"'형태에서 a와 b의 값을 알 수 있다.')
                    st.markdown('또한 두 점 사이의 거리가 지름이므로 ')
                    st.markdown(r"$(\frac{두 점 사이의 거리}{2})^2$"'를 통해서 'r"$r^2$"'의 값을 구할 수 있다.')
                    st.markdown('')
                    st.markdown('')
                    st.divider()
                    st.subheader('확인문제')
                    st.markdown('두 점 A(-4,2), B(6,2)를 지름의 양 끝으로 갖는 원의 방정식 'r"$(x-a)^2+(y-b)^2=c$"' 에 대하여 물음에 답하시오')
                    st.image('./img/check_pd.png')
                    check_pe1 =st.text_input('a의 값은 얼마인가?')
                    if check_pe1 == '1':
                        st.success('정답입니다.')
                    else:
                        st.error('오답입니다. 다시 생각해보세요.')
                    check_pe2 =st.text_input('b의 값은 얼마인가?')
                    if check_pe2 == '-2':
                        st.success('정답입니다.')
                    else:
                        st.error('오답입니다. 다시 생각해보세요.')
                    check_pe3 =st.text_input('C의 값은 얼마인가?')
                    if check_pe3 == '25':
                        st.success('정답입니다.')
                    else:
                        st.error('오답입니다. 다시 생각해보세요.')


                elif select == '세 점을 지나는 원의 방정식':
                    with open('./data/history.csv', 'a') as f:
                        f.write(f'{st.session_state["userid"]},page2_3,{nal}'+'\n')
                        f.close()        
                    st.subheader('세 점을 지나는 원의 방정식')
                    st.markdown('원이 지나는 세 점을 아는 경우 표준형 원의 방정식을 이용하여 보다 쉽게 구할 수 있다.')
                    st.markdown(r"$x^2+y^2+Ax+By+C=0$"'에 세 점의 좌표를 대입하면 미지수가 A,B,C 3개인 연립일차방정식이 만들어진다.')
                    st.markdown('연립일차 방정식의 해를 구하고 A,B,C의 값을 찾아낸다면 세 점을 지나는 원의 방정식을 구할 수 있다.')
                    st.markdown('')
                    st.markdown('')
                    st.divider()
                    st.subheader('확인문제')
                    st.markdown('세 점(-2,2),(4,-6),(5,-5)를 지나는 원의 방정식 'r"$x^2+y^2+Ax+By+C=0$"' 에 대하여 물음에 답하시오')
                    st.image('./img/check_pe.png')
                    check_pe1 =st.text_input('A의 값은 얼마인가?')
                    if check_pe1 == '-2':
                        st.success('정답입니다.')
                    else:
                        st.error('오답입니다. 다시 생각해보세요.')
                    check_pe2 =st.text_input('B의 값은 얼마인가?')
                    if check_pe2 == '4':
                        st.success('정답입니다.')
                    else:
                        st.error('오답입니다. 다시 생각해보세요.')
                    check_pe3 =st.text_input('C의 값은 얼마인가?')
                    if check_pe3 == '20':
                        st.success('정답입니다.')
                    else:
                        st.error('오답입니다. 다시 생각해보세요.')

                else:
                        st.info('is seeing nothing selected any items..')           
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

                    
            
                       