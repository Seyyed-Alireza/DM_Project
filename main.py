from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from questionOne import lowest_stations
from questionTwo import shortest_path

class QButton(QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent)

    def enterEvent(self, event):
        super().enterEvent(event) 
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def leaveEvent(self, event):
        super().leaveEvent(event) 
        self.unsetCursor()


app = QApplication([])

sz = QGuiApplication.primaryScreen().size()
screen_width = sz.width()
screen_height = sz.height()
window_width = int(0.6 * screen_width)
window_height = int(0.5 * screen_height)
default_x = int(0.2 * screen_width)
default_y = int(0.1 * screen_height)

window = QWidget()
window.setWindowTitle('Shortest Path')
window.setGeometry(default_x, default_y, window_width, window_height)
window.setFixedSize(window_width, window_height)
window.setStyleSheet('background-color: #fcebe5;')


def set_button_style(color, to_color, enabled=True):
    return f'''
    QPushButton {{
        background-color: {color if enabled else '#94daff'};
        color: white;
        font-size: {window_width // 64}px;
        border: 1px solid;
        border-radius: 3px;
    }}
    QPushButton:hover {{
        border: 2px solid;
    }}
    QPushButton:pressed {{
        font-size: {window_width // 64 - 1}px;
        background-color: {to_color};
    }}
    '''

def set_text_style(size, theme_light):
    return f'''
    QLabel {{
    font-size: {size}px;
    color: {'black' if theme_light else 'white'};
    font-family: 'calibri';
    }}'''

def set_combo_box_style(back_color, theme_light):
    return f'''
            QComboBox {{
                background-color: {back_color if theme_light else '#fcebe5'};
                color: {'#fcebe5' if theme_light else back_color};
                font-size: {window_width // 64}px;
                font-family: 'calibri';
                border-radius: 5px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {back_color if theme_light else '#fcebe5'};
                color: {'#fcebe5' if theme_light else 'black'};
                selection-background-color: #474747;
                padding: 5px;
                font-family: 'calibri';
                font-size: 18px;
            }}

            '''

def set_input_box_style(theme_light):
    return f'''
            QTextEdit {{
                border: 2px solid {'black' if theme_light else 'white'};
                border-radius: 5px;
                color: {'black' if theme_light else 'white'};
                font-size: 20px;
            }}
            QScrollBar:vertical {{
                border: none;
                background: #e0e0e0;
                width: 10px;
                border-radius: 5px;
            }}

            QScrollBar::handle:vertical {{
                background: #8f8f8f;
                border-radius: 5px;
            }}

            QScrollBar::handle:vertical:hover {{
                background: #404040;
            }}
            '''

groupbox_style = '''
QGroupBox {
    border: 2px solid black; 
    border-radius: 5px;
    margin-top: 6px; 
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 15px;
    padding: 0 5px;
    font-size: 20px;
}
'''

q1_test_case = '''4 2
Shiraz
Tehran
Isfahan
Mashhad
Shiraz Tehran
Mashhad Isfahan
Mashhad'''

q2_test_case = '''5 6
A
B
C
D
E
E C 136.81
D B 12.74
C B 14.63
B A 60.48
A D 45.63
A E 514.74
A
C'''


theme_light = True

question_groupbox = QGroupBox('Select Question', parent=window)
question_groupbox.setGeometry(int(0.05 * window_width), int(0.04 * window_height), int(0.9 * window_width), int(0.12 * window_height))
question_groupbox.setStyleSheet(groupbox_style)

q1_button = QButton('Question 1', parent=question_groupbox)
q1_button.setStyleSheet(set_button_style('#a4b55e', '#879451'))
q1_button.setGeometry(int(0.02 * question_groupbox.width()), int(0.3 * question_groupbox.height()), int(0.1 * question_groupbox.width()), int(0.55 * question_groupbox.height()))
q1_text = QLabel('--> Find shortset path based on number of stations', parent=question_groupbox)
q1_text.move(int(0.12 * question_groupbox.width()), int(0.4 * question_groupbox.height()))
q1_text.setStyleSheet(set_text_style(window_width // 64, 'black'))

q2_text = QLabel('--> Find shortset path based on distance', parent=question_groupbox)
q2_text.move(int(0.62 * question_groupbox.width()), int(0.4 * question_groupbox.height()))
q2_text.setStyleSheet(set_text_style(window_width // 64, 'black'))


q2_button = QButton('Question 2', parent=question_groupbox)
q2_button.setStyleSheet(set_button_style('#a4b55e', '#879451'))
q2_button.setGeometry(int(0.52 * question_groupbox.width()), int(0.3 * question_groupbox.height()), int(0.1 * question_groupbox.width()), int(0.55 * question_groupbox.height()))


# ---------------------------------------------Menu---------------------------------------- #
menu_groupbox = QGroupBox('Menu', parent=window)
menu_groupbox.setGeometry(int(0.05 * window_width), int(0.19 * window_height), int(0.65 * window_width), int(0.12 * window_height))
menu_groupbox.setStyleSheet(groupbox_style)

close_button = QButton('Close', parent=menu_groupbox)
close_button.setStyleSheet(set_button_style('#17a3ee', '#1274ff'))
close_button.setGeometry(int(0.03 * menu_groupbox.width()), int(0.3 * menu_groupbox.height()), int(0.17 * menu_groupbox.width()), int(0.55 * menu_groupbox.height()))
close_button.clicked.connect(window.close)

reset_button = QButton('Reset', parent=menu_groupbox)
reset_button.setStyleSheet(set_button_style('#17a3ee', '#1274ff'))
reset_button.setGeometry(int(0.23 * menu_groupbox.width()), int(0.3 * menu_groupbox.height()), int(0.17 * menu_groupbox.width()), int(0.55 * menu_groupbox.height()))


clear_button = QButton('Clear', parent=menu_groupbox)
clear_button.setStyleSheet(set_button_style('#17a3ee', '#1274ff', enabled=False))
clear_button.setGeometry(int(0.43 * menu_groupbox.width()), int(0.3 * menu_groupbox.height()), int(0.17 * menu_groupbox.width()), int(0.55 * menu_groupbox.height()))
clear_button.setEnabled(False)

submit_button = QButton('Submit', parent=menu_groupbox)
submit_button.setStyleSheet(set_button_style('#17a3ee', '#1274ff', enabled=False))
submit_button.setGeometry(int(0.63 * menu_groupbox.width()), int(0.3 * menu_groupbox.height()), int(0.17 * menu_groupbox.width()), int(0.55 * menu_groupbox.height()))
submit_button.setEnabled(False)

#------------------------------------------------------ Answer Text Box ---------------------------------------#
answer_text_box = QTextEdit(parent=window)
answer_text_box.move(int(0.35 * window_width), window_height)
answer_text_box.resize(int(0.5 * window_width), int(0.3 * window_height))
answer_text_box.setStyleSheet(set_input_box_style(theme_light))
answer_text_box.setReadOnly(True)

answer_text = QLabel('Answer -->', parent=window)
answer_text.setStyleSheet(set_text_style(window_width // 42, theme_light))
answer_text.adjustSize()
answer_text.move(int(0.35 * window_width) - int(answer_text.width() * 1.2), int(1.11 * window_height))

def answer_text_changed():
    answer_text_box.setStyleSheet(set_input_box_style(theme_light))
answer_text_box.textChanged.connect(answer_text_changed)
#--------------------------------------------------------------------------------------------------------------#

window_extended = False
def extend_window():
    global theme_light
    global window_extended
    if ques == None or ques not in (1, 2):
        error_text.setText('Fisrt select a question')
        error_text.adjustSize()
        error_text.move(int(0.35 * window_width) - int(wh_text.width() * 1.1) + (wh_text.width() // 2) - int(error_text.width() // 2), int(0.55 * window_height) + int(1.2 * wh_text.height()) + int(1.2 * test_case_button.height()))
        return
    else:
        error_text.setText('')
    if not window_extended:
        window.setGeometry(default_x, default_y, window_width, window_height + int(0.4 * window_height))
        window.setFixedSize(window_width, window_height + int(0.4 * window_height))

        window_extended = True
    answer_text_box.setText('')
    answer = lowest_stations(input_box.toPlainText()) if ques == 1 else shortest_path(input_box.toPlainText())
    if answer == 'invalid':
        answer_text_box.setText(f'Invalid input for question {ques}')
    else:
        answer_text_box.setText(answer)
    
submit_button.clicked.connect(extend_window)

theme_box = QComboBox(parent=menu_groupbox)
theme_box.setGeometry(int(0.83 * menu_groupbox.width()), int(0.3 * menu_groupbox.height()), int(0.15 * menu_groupbox.width()), int(0.55 * menu_groupbox.height()))
theme_box.addItems(['Light', 'Dark'])
theme_box.setStyleSheet(set_combo_box_style('#3b3b3b', theme_light))

#--------------------------------------------------------- Change Theme --------------------------------------#
def change_theme(index):
    global theme_light
    if index == 0:
        theme_light = True
        window.setStyleSheet('background-color: #fcebe5;')
    else:
        theme_light = False
        window.setStyleSheet('background-color: #403b39;')
    answer_text.setStyleSheet(set_text_style(window_width // 42, theme_light))
    wh_text.setStyleSheet(set_text_style(window_width // 42, theme_light))
    theme_box.setStyleSheet(set_combo_box_style('#3b3b3b', theme_light))
    selected_question.setStyleSheet(set_text_style(window_width // 52, theme_light))
    q1_text.setStyleSheet(set_text_style(window_width // 64, theme_light))
    q2_text.setStyleSheet(set_text_style(window_width // 64, theme_light))
    input_box.setStyleSheet(set_input_box_style(theme_light))
    answer_text_box.setStyleSheet(set_input_box_style(theme_light))
theme_box.currentIndexChanged.connect(change_theme) 
#--------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------#

#------------------------------------ Show Selected Question --------------------------------------------------#
ques = None
def set_ques(num):
    global ques
    ques = num
    selected_question.setText(f'Question {ques} selected')
q1_button.clicked.connect(lambda: set_ques(1))
q2_button.clicked.connect(lambda: set_ques(2))
selected_question = QLabel('No question selected' if ques == None else f'question {ques} selected', parent=window)
selected_question.move(int(0.73 * window_width), int(0.23 * window_height))
selected_question.setStyleSheet(set_text_style(window_width // 52, 'black'))
#--------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------- Input Textbox ---------------------------------------#
wh_text = QLabel('Write input here -->', parent=window)
wh_text.setStyleSheet(set_text_style(window_width // 42, theme_light))
wh_text.adjustSize()
wh_text.move(int(0.35 * window_width) - int(wh_text.width() * 1.1), int(0.55 * window_height))
input_box = QTextEdit(parent=window)
input_box.move(int(0.35 * window_width), int(0.4 * window_height))
input_box.resize(int(0.5 * window_width), int(0.5 * window_height))
input_box.setStyleSheet(set_input_box_style(theme_light))
test_case_button = QButton('Paste TestCase', parent=window)
test_case_button.setStyleSheet(set_button_style('#6036ab', "#5114bb"))
test_case_button.adjustSize()
test_case_button.move(int(0.35 * window_width) - int(wh_text.width() * 1.1) + (wh_text.width() // 2) - (int(test_case_button.width() * 1.2) // 2), int(0.55 * window_height) + int(1.2 * wh_text.height()))
test_case_button.resize(int(1.2 * test_case_button.width()), int(1.2 * test_case_button.height()))
error_text = QLabel('', parent=window)
error_text.setStyleSheet(set_text_style(window_width // 64, theme_light))
error_text.adjustSize()
error_text.move(int(0.35 * window_width) - int(wh_text.width() * 1.1) + (wh_text.width() // 2) - int(error_text.width() // 2), int(0.55 * window_height) + int(1.2 * wh_text.height()) + int(1.2 * test_case_button.height()))
def test_case_click():
    if ques == None:
        error_text.setText('Fisrt select a question')
        error_text.adjustSize()
        error_text.move(int(0.35 * window_width) - int(wh_text.width() * 1.1) + (wh_text.width() // 2) - int(error_text.width() // 2), int(0.55 * window_height) + int(1.2 * wh_text.height()) + int(1.2 * test_case_button.height()))
        return
    else:
        error_text.setText('')
    input_box.setText(q1_test_case if ques == 1 else q2_test_case)
    extend_window()
test_case_button.clicked.connect(test_case_click)

def input_text_changed():
    text = input_box.toPlainText()
    not_empty = bool(text.strip())
    clear_button.setEnabled(not_empty)
    submit_button.setEnabled(not_empty)
    input_box.setStyleSheet(set_input_box_style(theme_light))
    clear_button.setStyleSheet(set_button_style('#17a3ee', '#1274ff', enabled=not_empty))
    submit_button.setStyleSheet(set_button_style('#17a3ee', '#1274ff', enabled=not_empty))

def clear_text():
    input_box.setText('')
    answer_text_box.setText('')
    # window.setGeometry(default_x, default_y, window_width, window_height)

input_box.textChanged.connect(input_text_changed)
clear_button.clicked.connect(clear_text)
#--------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------- Reset Everything ------------------------------------#
def reset_all():
    global window_extended
    window.setGeometry(default_x, default_y, window_width, window_height)
    window.setFixedSize(window_width, window_height)
    window_extended = False
    global theme_light
    theme_box.setCurrentIndex(0)
    theme_light = True
    input_box.setText('')
    answer_text_box.setText('')
    global ques
    ques = None
    selected_question.setText('No question selected')
    error_text.setText('')
reset_button.clicked.connect(reset_all)


window.show()
app.exec_()