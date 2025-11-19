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
    if not task: return
    if 'word' not in st.session_state: st.session_state.word = ''
    col1,col2 = st.columns(2)
    col1.title('Word:')
    if isinstance(st.session_state.word, str): col2.title(f'Result: {st.session_state.word}')

    with st.form('Fill in the gap'):
        parts = task.split('/')
        st.write('debug parts', parts)
        options = parts[1].split('.')
        good_option = parts[-1]
        display_options = options[:]
        selected_option = st.selectbox(parts[0], options=display_options, index=2)
        #selected_option = st.text_input(f'Options:{display_options}')
        submit = st.form_submit_button('Check')

    st.session_state.word = f'You say: {selected_option}:{selected_option.strip() == good_option.strip()}'
    if submit: st.rerun()

'''
I change my strategy. The user should write the entire phrase into the text_input. Then I just compare.
I am tired of this Forms mess.
'''

def checkTask(task):
    parts = task.split('/')
    st.write('debug parts', parts)
    options = parts[1].split('.')
    good_option = parts[-1]
    good_phrase = parts[0].replace('X', good_option)
    st.session_state.good_phrase = good_phrase
    st.write('debug good phrase', good_phrase)
    st.session_state.selected_option = st.text_input(parts[0])

def PrintTasks(subjects):
    if 'selected_option' in st.session_state and 'good_phrase' in st.session_state:
        st.write("Check", st.session_state.selected_option, ';', st.session_state.good_phrase)
    level = str(st.slider('Waehle das Level aus:', 1, 3))
    amount = st.slider('Waehle wieviele Aufgaben:', 1, 10)
    subject = st.selectbox(label="Waehle das Fach: ", options=subjects, index=1)
    Tasks = CleanTasks(ReadSubjectFile(subject, level))
    if Tasks == None: st.error("File not found"); exit()
    task = XTasks(Tasks, 1)[0]
    checkTask(task)

def run(name, level, subjects):
    st.header("Repeat what you heard")
    s1 = Student(name, level, subjects)
    st.header(f"Welcome {name} to your Dynamic Teaching Generator:\n")
    PrintTasks(s1.subjects)

if __name__ == '__main__':
    subjects = ['german', 'english', 'math', 'art']
    ReadAllFiles(subjects)
    run('Johnny', 5, subjects)