import streamlit as st
from datetime import datetime as dt

if "mygrades" not in st.session_state:
    st.session_state.mygrades = []

if "tskclk" not in st.session_state:
    st.session_state.tskclk = []

if "chkarr" not in st.session_state:
    st.session_state.chkarr = []

if "rerun" not in st.session_state:
    st.session_state.rerun = False


def cmpltTask(task):
    idx = st.session_state.mygrades.index(task)
    st.session_state.chkarr[idx] = not st.session_state.chkarr[idx]
    st.session_state.rerun = True

def listTasks():
    st.session_state.tskclk = []
    for i, task in enumerate(st.session_state.mygrades):
        st.session_state.tskclk.append(st.checkbox(task, value = st.session_state.chkarr[i], key = 'l' + f'{dt.now():%d%m%Y%H%M%S%f}', on_change = cmpltTask, args=(task,), help ='Check to mark as completed'))


if st.session_state.rerun == True:
    st.session_state.rerun = False
    st.experimental_rerun()

else:
    grade = st.number_input('Noten eingeben', value="", placeholder = 'Eine Note eingeben')
    if st.button('Note hinzufügen'):
        if grade != "":
            st.session_state.mygrades.append(grade)
            st.session_state.chkarr.append(False)

listTasks()