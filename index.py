import sys
import random as r
import streamlit as st

class Student:
    def __init__(self, name, level, subjects):
        self.name = name
        self.level = level
        self.subjects = subjects

def ReadAllFiles(subjects):
    if 'all_files' in st.session_state: return
    print("Reading from Disk")
    all_files = {}
    for subject in subjects:
        all_files[subject] = {}
        for level in range(1, 4):
            try: all_files[subject][f'level{str(level)}'] = open("subjects/" + subject + '/' + subject + '_level' + str(level) + '.txt', 'r').read().splitlines()
            except Exception as e: print(e); continue
    st.session_state['all_files'] = all_files

def ReadSubjectFile(subject, level):
    return st.session_state['all_files'][subject][f'level{level}']

def CleanTasks(all_level_tasks):
    if all_level_tasks == None: return None
    return ''.join(all_level_tasks).split('**=END=**')

def XTasks(tasks, x):
    if x <= len(tasks): return r.sample(tasks, x)
    return r.sample(tasks, len(tasks))

def checkSelectedOption(selected_option, good_option):
    if selected_option == None: return -1
    if selected_option == good_option: st.success("GOOD"); return True
    st.error("error"); return False

def PrintRiddle(task):
    parts = task.split('/')
    #try:
    options = parts[1].split('.')
    good_option = options[:-1]
    r.shuffle(options)
    selected_option = st.selectbox(parts[0], options=options, index=None, placeholder='Select')
    outcome = checkSelectedOption(selected_option, good_option)
    #except Exception as e: print(e); return

def show_form(task):
    if 'sum' not in st.session_state: st.session_state.sum = ''
    if 'selected_option' not in st.session_state: st.session_state.selected_option = ''
    if 'good_option' not in st.session_state: st.session_state.good_option = ''
    col1,col2 = st.columns(2)
    col1.title('Sum:')
    if isinstance(st.session_state.sum, bool):
        col2.title(f'Result: {st.session_state.sum}')

    ####

    st.write('task:', task)
    parts = task.split('/')
    st.write('debug parts', parts)
    options = parts[1].split('.')
    good_option = options[-1]
    st.write('options:', options, '\ngood option:', good_option)
    st.session_state.good_option = good_option
    display_options = options[:]
    r.shuffle(display_options)
    selected_option = ''
    ####

    with st.form('addition'):
        parts = task.split('/')
        st.write('debug parts', parts)
        options = parts[1].split('.')
        good_option = options[-1]
        st.write('options:', options, '\ngood option:', good_option)
        selected_option = st.selectbox(parts[0], options=display_options, index=2)
        st.write('selected_option:', selected_option, '\ngood_option:', good_option)
        st.session_state.selected_option = selected_option
        a = st.text_input('a')
        b = st.text_input('b')
        submit = st.form_submit_button('Check')

    # The value of st.session_state.sum is updated at the end of the script rerun,
    # so the displayed value at the top in col2 does not show the new sum. Trigger
    # a second rerun when the form is submitted to update the value above.
    st.session_state.sum = a == b#selected_option.strip() == good_option.strip()#a == b#
    if submit:
        st.rerun()

def PrintTasks(subjects):
    level = str(st.slider('Waehle das Level aus:', 1, 3))
    amount = st.slider('Waehle wieviele Aufgaben:', 1, 10)
    subject = st.selectbox(label="Waehle das Fach: ", options=subjects, index=1)
    Tasks = CleanTasks(ReadSubjectFile(subject, level))
    if Tasks == None: st.error("File not found"); exit()
    #tasks = XTasks(Tasks, amount)
    task = Tasks[0]
    #for task in tasks: 
    show_form(task)

def run(name, level, subjects):
    st.header("Repeat what you heard")
    s1 = Student(name, level, subjects)
    st.header(f"Welcome {name} to your Dynamic Teaching Generator:\n")
    PrintTasks(s1.subjects)

if __name__ == '__main__':
    subjects = ['german', 'english', 'math', 'art']
    ReadAllFiles(subjects)
    run('Johnny', 5, subjects)