import streamlit as st
import openai


st.set_page_config(layout="wide")

if 'userid' not in st.session_state:
    st.error('로그인을 한 후 이용하세요!')
elif 'ansdata' not in st.session_state:
    st.error('문제풀이를 완료하고 돌아오세요!')
else:
    ansdata = st.session_state['ansdata']
    userId = st.session_state['userid']
    st.info(f'{userId} 학생의 정오표')

    checksum = 0

    for i in range(len(ansdata)):
        if ansdata[i] == f'{i+1}번 정답':
            st.success(ansdata[i])
        else:
            st.error(ansdata[i])
            checksum += 1

    st.divider()
    pul = ['오답풀이 1', '오답풀이 2', '오답풀이 3', '오답풀이 4','오답풀이 5']

    if checksum == 0:
        st.markdown('**축하합니다. 모두 정답입니다~**')
    else:
        cl1, cl2 = st.columns((15, 5))
        with cl1:
            if ansdata[0] == "1번 오답":
                pul[0]
                st.markdown('원의 중심이 (3,-1)이고 반지름의 길이가 2인 원의 방정식은')   
                st.markdown(r"$(x-3)^2+(y+1)^2=(2)^2$"'이다.')
                st.markdown('따라서'r"$a=3, b=4$",help="반지름의 길이의 제곱이 b의 값이 됨에 주의한다.")
                st.markdown('이며, a+b의 값은 7이다.')
                st.markdown('')
                st.divider()
                
            else:
                pass
            
            if ansdata[1] == "2번 오답":
                pul[1]
                st.markdown('중점(2,-6)을 갖고 반지름이 r인 원의 방정식은')
                st.markdown(r"$(x-2)^2+(y+6)^2=(r)^2$"'이며 괄호를 계산하면')
                st.markdown(r"$x^2-4x+4+y^2+12y+36=r^2$"'이고 식을 정리하면')
                st.markdown(r"$x^2+y^2-4x+12y+(4+36-r^2)=0$"'이 된다.')
                st.markdown('따라서 A=-4, B=12이므로 합은 8이다.')
                st.markdown('')
                st.divider()
                
            else:
                pass
            
            if ansdata[2] == "3번 오답":
                pul[2]
                
                st.markdown('두 점의 좌표가 주어졌으므로 차례대로 밑의 방정식에 대입하면 다음과 같다.')
                st.markdown(r"$a^2+9=b$"'······· ㉠')
                st.markdown(r"$a^2+2a+1+4=b$"'······· ㉡')
                st.markdown(r"$(k+1)^2+(-2)^2-r^2=k^2+2k+5-r^2=0$"'')
                st.markdown('㉠과 ㉡을 연립하면 a=2, b=13이다.')
                st.markdown('따라서 a+b의 값은 15이다.')
                st.markdown('')
                st.divider()
            else:
                pass
            
            if ansdata[3] == "4번 오답":
                pul[3]
                st.markdown('지름의 양 끝점이 주어질 경우 원의 중심은 두 점의 중점이 된다.')
                st.markdown('따라서 원의 중심은 두 점의 중점인(4,7)이고 a+b는 11이다.')
                st.markdown('')
                st.divider()
            
            else:
                pass
            
            if ansdata[4] == "5번 오답":
                pul[4]
                st.markdown('세 점의 좌표를 차례대로 문제의 방정식에 대입하면 다음과 같다.')
                st.markdown(r"$a^2+2a+1+b^2=c$"'······· ㉠')
                st.markdown(r"$a^2-6a+9=b^2=c$"'······· ㉡')
                st.markdown(r"$a^2-2a+1+b^2-4b+4=c$"'······· ㉢')
                st.markdown('㉠과㉡을 연립하면 a=1이다.')
                st.markdown('이를 이용하여 ㉡과 ㉢을 연립하여 b와 c의 값을 구하면 b=0,c=4이다.')
                st.markdown('따라서 a+b+c=5이다.')
                st.markdown('')
                st.markdown('')
                st.divider()
            else:
                pass
        with cl2:
            with st.expander('Tip'):            
                st.markdown('풀이가 이해하기 어려우면 ',help ='이 버튼을 찾아보세요!')
                st.markdown('버튼을 눌러보세요!')
