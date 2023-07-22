import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

nal = datetime.datetime.now()

if 'userid' not in st.session_state:
    st.session_state['userid'] = 'Anonymous'

if 'passwd' not in st.session_state:
    st.session_state['passwd'] = 'Anonymous'



st.title('LOGIN을 진행해주세요')
with st.expander('New User Register : '):
    with st.form('Register'):
        userid = st.text_input('Email: ')
        username = st.text_input('UserName: ')
        passwd = st.text_input('PassWD: ', type='password')

        if st.form_submit_button('Register'):
            if all([userid, username, passwd]):
                with open('./data/userdb.csv', 'a') as f:
                    txt = f'{userid},{username},{passwd}\n'
                    f.write(txt)
                    f.close()
                st.info('Register 성공! 로그인을 진행해주세요.')
            else:
                st.error('Register 실패')

if st.session_state['userid'] != 'Anonymous':
    st.info(f'{st.session_state["userid"]} is already logged in!!')
    dfa = pd.read_csv('./data/history.csv', encoding='cp949')
    
    
else:
    with st.expander('Login...'):
        with st.form('login'):
            userid = st.text_input('UserID: ')
            passwd = st.text_input('PassWD: ', type='password')

            if st.form_submit_button('Login'):
                if all([userid, passwd]):
                    df = pd.read_csv('./data/userdb.csv', encoding='cp949')
                    useridList = list(df.iloc[:, 0])
                    passwdList = list(df.iloc[:, -1])
                    usernameList = list(df.iloc[:, 1])

                    if userid in useridList:
                        if passwd in passwdList:
                            st.info(f'Welcome!!! {userid}. Success!!')
                            st.session_state['userid'] = userid
                            st.experimental_rerun()
                        else:
                            st.error('Wrong Passwd')
                    else:
                        st.error('학생ID가 등록되어 있지 않습니다. Register 먼저 해주세요!')
                else:
                    st.error('로그인 실패, 패스워드를 다시 확인해주세요.')

# st.title('머신러닝 Digital Textbook')
# # 학습경로는 순서대로 늘어난다.
# if st.session_state['userid'] != 'Anonymous':
#     dfa = pd.read_csv('./data/history.csv', encoding='cp949') #cp949로 바꾸면 한글입력 가능 utf-8(영어용)
#     # st.write(df)
#     if len(dfa.iloc[:, 0]) > 1:
#         df = dfa.iloc[:,:]
#         pathWay = list(df[df.iloc[:, 0] == f'{st.session_state["userid"]}'].iloc[:, 1])
#         # pathWay.pop()
#     else:
#         st.info('아직 패스웨이 데이터가 없습니다.')
#     pathList = ''
#     for i in pathWay:
#         pathList += i + '/'

#     dictPath = {}
#     for i in pathList.split('/'):
#         if i in dictPath:
#             dictPath[i] += 1
#         else:
#             dictPath[i] = 1
#     plt.rcParams['font.family'] ='Malgun Gothic'
#     plt.rcParams['axes.unicode_minus'] =False

#     dfPath = pd.DataFrame(dictPath, index=[0]).T
#     dfPath.columns = ['빈도']
#     fig, ax = plt.subplots()
#     ax.bar(dfPath.index, dfPath['빈도'])
#     ax.set_xlabel('경로')
#     ax.set_ylabel('빈도')
#     ax.set_title(f'{st.session_state["userid"]}의 학습경로 빈도')
#     ax.tick_params(axis='x', rotation=90)
#     st.pyplot(fig)

# else:
#     st.subheader('로그인을 해주세요!')
#     # st.subheader(f'{st.session_state["userid"]}의 학습경로: root/')

# if st.session_state['userid'] != 'Anonymous':
#     pass
# else:
#     userid = st.text_input('Input userID: ')
#     passwd = st.text_input('Password: ', type='password')

# if st.session_state['userid'] != 'Anonymous':
#     # with open('./data/history.csv', 'a') as f:
#     #     f.write(f'{st.session_state["userid"]},Login_True,{nal}'+'\n')
#     #     f.close()
#     st.success(f'{st.session_state["userid"]}님, 이미 로그인이 되었습니다.')  
# else:
#     if all([userid, passwd]):
#         # with open('./data/history.csv', 'a') as f:
#         #     f.write(f'{st.session_state["userid"]},Login_True,{nal}'+'\n')
#         #     f.close()
#         st.session_state['userid'] = userid
#         st.session_state['passwd'] = passwd
#         st.success(f'{st.session_state["userid"]}님, 로그인 성공')

#     else:
#         # with open('./data/history.csv', 'a') as f:
#         #     f.write(f'{st.session_state["userid"]},Login_False,{nal}'+'\n')
#         #     f.close()
#         st.error('모든 정보는 입력해야 합니다.')