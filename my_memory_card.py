from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QButtonGroup, QPushButton 
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
      self.question = question
      self.right_answer = right_answer
      self.wrong1 = wrong1
      self.wrong2 = wrong2
      self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государствиный язык Бразилии', 'Португалский', 'Бразилский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Какого цвета нет на флаге России?','Зелёный','Красный','Синий','Белый'))
questions_list.append(Question('Националньая хижина якутов','Урста','Юрта','Иглу','Хата'))
questions_list.append(Question('Назови ствлицу Японийи?','Токийо','Хиросима','Осака','Кийото'))
questions_list.append(Question('Ты кто?','Человек','НЕ ЗНАЮ!!!','Котик','Никто'))
questions_list.append(Question('Какая страна выйграла чемпионат мира?','Аргентина','Бразилия','Харватия','Поругалия'))
app = QApplication([])
window = QWidget()
window.total = 0
window.score = 0
window.setWindowTitle('Угадайка???')
    
btn_OK = QPushButton('Ответить')

lb_Question = QLabel('В каком году родился Пушкин')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1799')
rbtn_2 = QRadioButton('1809')
rbtn_3 = QRadioButton('1800')
rbtn_4 = QRadioButton('1790')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
#создай приложение для запоминания информации
layout_ans_hor = QHBoxLayout()
layout_ans_ver1 = QVBoxLayout()
layout_ans_ver2 = QVBoxLayout()
layout_ans_ver1.addWidget(rbtn_1)
layout_ans_ver1.addWidget(rbtn_2)
layout_ans_ver2.addWidget(rbtn_3)
layout_ans_ver2.addWidget(rbtn_4)

layout_ans_hor.addLayout(layout_ans_ver1)

layout_ans_hor.addLayout(layout_ans_ver2)

RadioGroupBox.setLayout(layout_ans_hor)

AnsGroupBox = QGroupBox("Резултаты теста")
lb_Result = QLabel('пав ты или нет?')

lb_Correct = QLabel('Ответ будет тут')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=1)

AnsGroupBox.setLayout(layout_res)



layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter|
Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()



#RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addStretch(1)
layout_card.addLayout(layout_line1)
layout_card.addStretch(1)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3)
layout_card.addStretch(1)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следуший вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q: Question):

    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def next_question():
    window.total += 1
    print('Статистика\n-Всего вапросов: ' ,window.total, '\n-Правилных ответов: ', window.score )
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    #window.cur_question = window.cur_question + 1
    #if window.cur_question >= len(questions_list):
        #window.cur_question = 0
    
    q = questions_list[cur_question]
    ask(q)

def check_answer():
    if answers[0].isChecked():
        show_correct('Правилно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правилных ответов: ', window.score )
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100),)


def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


window.cur_question = -1

btn_OK.clicked.connect(click_OK)

'''
def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()
'''



next_question()
window.setLayout(layout_card)
window.show()
app.exec()



