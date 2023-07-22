import streamlit as st
import datetime
import pandas as pd
import openai

st.set_page_config(layout="wide")

nal = datetime.datetime.now()
if 'userid' not in st.session_state:
    st.error('로그인을 한 후 이용하세요!')
elif 'scheck' not in st.session_state:
    st.error('문제풀이를 완료하고 돌아오세요!')
else:
    scheck = st.session_state['scheck']
    userId = st.session_state['userid']
    st.info(f'{userId} 학생의 틀린 개념 보충하기')
    
    if scheck[0] == "F":
        st.markdown('1번 문제 개념 : **원의 방정식(1)**')
        with open('./data/history.csv', 'a') as f:
                        f.write(f'{st.session_state["userid"]},page1_1,{nal}'+'\n')
                        f.close()
    if scheck[1] == "F":
        st.markdown('2번 문제 개념 : **원의 방정식(2)**')
        with open('./data/history.csv', 'a') as f:
                        f.write(f'{st.session_state["userid"]},page1_2,{nal}'+'\n')
                        f.close()
    if scheck[2] == "F":
        st.markdown('3번 문제 개념 : **한 점을 중점으로 갖고 한 점을 지나는 원의 방정식**')
        with open('./data/history.csv', 'a') as f:
                        f.write(f'{st.session_state["userid"]},page2_1,{nal}'+'\n')
                        f.close()
    if scheck[3] == "F":
        st.markdown('4번 문제 개념 : **두 점을 지름의 끝으로 같는 원의 방정식**')
        with open('./data/history.csv', 'a') as f:
                        f.write(f'{st.session_state["userid"]},page2_2,{nal}'+'\n')
                        f.close()  
    if scheck[4] == "F":
        st.markdown('5번 문제 개념 : **세 점을 지나는 원의 방정식**')
        with open('./data/history.csv', 'a') as f:
                        f.write(f'{st.session_state["userid"]},page2_3,{nal}'+'\n')
                        f.close() 
    st.divider()

    if scheck[0] == "F":
        st.subheader('원의 방정식(1)')
        st.markdown('좌표평면 위의 한 점 C(a, b)를 중심으로 하고 반지름의 길이가 r인 원을 나타내는 방정식을 알아보자.')
        st.markdown('이 원 위의 임의의 점을 P(x, y)라고 하면 CP=r이므로')
        st.markdown(r"$\sqrt{(x-a)^2+(y-a)^2}= r$")
        st.markdown('이다. 이 식의 양변을 제곱하면')
        st.markdown(r"$(x-a)^2+(y-b)^2=r^2$"'······· ㉠')
        st.markdown('이다. 한편, 점 P(x, y)가 ㉠을 만족시키면 선분CP의 길이는 r이므로 점 P(x, y)는 중심이 C(a,b)이고 반지름의 길이가 r인 원 위의 점이다.')
        st.markdown('따라서 ㉠을 점 C(a, b)를 중심으로 하고 반지름의 길이가 r인 원의 방정식이라고한다.')
        st.markdown('앞의 내용을 정리하면 다음과 같다.')
        st.image('./img/원의 방정식 정리.png')        
        st.divider()
        
    else:
        pass
    
    if scheck[1] == "F":
        st.subheader('원의 방정식(2)')
        st.markdown('원의 방정식을 전개하여 정리하면')
        st.markdown(r"$x^2+y^2-2ax-2yx+a^2+b^2=0$"'이다.')
        st.markdown('이때 'r"$-2a=A, -2b=B, a^2+b^2=C$")
        st.markdown('라고 한다면 이 원의 방정식은')
        st.markdown(r"$x^2+y^2+Ax+By+C=0$")
        st.markdown('꼴로 나타낼 수 있다.')
        st.markdown('또한, 위의 x,y에 대한 이차방정식은')
        st.markdown(r"$(x+\frac{A}{2})^2+(y+\frac{B}{2})^2=\frac{A^2+B^2+C}{4}$")
        st.markdown('로 변형할 수 있다. 이때'r"$A^2+B^2-4C>0$"'이면')
        st.markdown('중심이 점'r"$(-\frac{A}{2},-\frac{B}{2})$"'이고, 반지름의 길이가 'r"$\frac{\sqrt{A^2+B^2-4C}}{2}$"'인 원을 나타낸다.')
        
        st.divider()
        
    else:
        pass
    
    if scheck[2] == "F":
        st.subheader('한 점을 중점으로 갖고 한 점을 지나는 원의 방정식')
        st.markdown('두 점을 지름의 끝으로 갖는 경우, 두 점의 중점이 원의 중심이 된다.')
        st.markdown('따라서 표준형인 'r"$(x-a)^2+(y-b)^2=r^2$"'형태에서 a와 b의 값을 알 수 있다.')
        st.markdown('또한 두 점 사이의 거리가 지름이므로 ')
        st.markdown(r"$(\frac{두 점 사이의 거리}{2})^2$"'를 통해서 'r"$r^2$"'의 값을 구할 수 있다.')
        
        st.divider()
    else:
        pass
    
    if scheck[3] == "F":
        st.subheader('두 점을 지름의 끝으로 같는 원의 방정식')
        st.markdown('두 점을 지름의 끝으로 갖는 경우, 두 점의 중점이 원의 중심이 된다.')
        st.markdown('따라서 표준형인 'r"$(x-a)^2+(y-b)^2=r^2$"'형태에서 a와 b의 값을 알 수 있다.')
        st.markdown('또한 두 점 사이의 거리가 지름이므로 ')
        st.markdown(r"$(\frac{두 점 사이의 거리}{2})^2$"'를 통해서 'r"$r^2$"'의 값을 구할 수 있다.')
        st.divider()
       
    else:
        pass
    
    if scheck[4] == "F":
        st.subheader('세 점을 지나는 원의 방정식')
        st.markdown('원이 지나는 세 점을 아는 경우 표준형 원의 방정식을 이용하여 보다 쉽게 구할 수 있다.')
        st.markdown(r"$x^2+y^2+Ax+By+C=0$"'에 세 점의 좌표를 대입하면 미지수가 A,B,C 3개인 연립일차방정식이 만들어진다.')
        st.markdown('연립일차 방정식의 해를 구하고 A,B,C의 값을 찾아낸다면 세 점을 지나는 원의 방정식을 구할 수 있다.')
       
        st.divider()
    else:
        pass