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
    st.title('배운 내용 정리하기')
    cl1, cl2 = st.columns((15, 5))
    with cl1:
        st.write('1. 아래의 그림은 원의 중심이 (3, -1)이고 반지름의 길이가 2인 원의 방정식 'r"$(x-a)^2+(y+1)^2=b$"'이다. 이때, a+b의 값을 구하시오.')
        st.image('./img/문제1번.png')
        

        st.write('2. 원의 방정식'r"$x^2+y^2+Ax^2+By^2+C=0$"'에서 원의 중점이 (2,-6)이 되게하는 A,B 값의 합을 구하시오' )


        st.write('3. 중심이 x축 위에 있고, 두 점 (0, 3), (-1, -2)를 지나는 원의 방정식 'r"$(x-a)^2+y^2=b$"'가 있다. 이때, a+b의 값을 구하시오.')


        st.write('4. 두 점 (2, 6), (6, 8)을 지름의 양 끝점으로 하는 원의 중심의 좌표를 (a, b)라 할 때, a+b의 값을 구하시오.')


        st.write('5. 세 점 A(-1, 0), B(3, 0), C(1, 2)를 지나는 원의 방정식 'r"$(x-a)^2+(y-b)^2=c$"'가 있다. 이때, a+b+c의 값을 구하시오.')

    with cl2:
        with st.form('답안 작성'):
            
            ansdata=['', '', '','','']
            scheck =['','','','','']
            ans = ['7', '8', '15', '14', '5']
            sAns = ['','','','','']
            sAns[0] = st.text_input('1번')
            sAns[1] = st.text_input('2번')
            sAns[2] = st.text_input('3번')
            sAns[3] = st.text_input('4번')
            sAns[4] = st.text_input('5번')

            for i in range(len(ansdata)):
                if sAns[i]=='':
                    pass       
                elif sAns[i] == ans[i]:
                    ansdata[i] = f'{i+1}번 정답'
                    scheck[i] = 'complete'
                else:
                    ansdata[i] = f'{i+1}번 오답'
                    scheck[i] = 'F'
        
            if st.form_submit_button('Submit'):                
                if all ([sAns[0], sAns[1], sAns[2], sAns[3], sAns[4]]):
                    with open('./data/stAns.csv', 'a') as f:
                        f.write(f'{st.session_state["userid"]},{sAns[0]},{sAns[1]},{sAns[2]},{sAns[3]},{sAns[4]},{nal}'+'\n')
                        f.close()
                    st.session_state['ansdata'] = ansdata
                    with open('./data/LearningComplete.csv', 'a') as f:
                        f.write(f'{st.session_state["userid"]},{scheck[0]},{scheck[1]},{scheck[2]},{scheck[3]},{scheck[4]},{nal}'+'\n')
                        f.close()
                    st.session_state['scheck'] = scheck
                    with open('./data/history.csv', 'a') as f:
                        f.write(f'{st.session_state["userid"]},ans_submit,{nal}'+'\n')
                        f.close()
                    st.success('제출완료')
                else:
                    st.error('답을 모두 입력해주세요.')