from tkinter import *
import unittest
from math import *
import math



class BTN(Button):
    # 自定义按钮类，设置显示文本你，显示为位置，以及对应函数
    def __init__(self,frame,text,fun, args,bg='white',fg='black'):
        super(BTN,self).__init__()
        self.x,self.y,self.w,self.h = args[0],args[1],args[2],args[3]
        self.btn = Button(frame,text=text,bg=bg,fg=fg,command=fun).place(x=self.x, y=self.y, width=self.w, height=self.h)


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("科学计算器")
        self.master.geometry('560x420')  # 设置主窗口的初始尺寸
        self.master.resizable(0, 0)
        self.result = StringVar()  # 用于显示结果的可变文本
        self.equation = StringVar()  # 显示计算方程
        self.screen_equation = StringVar()  # 实际用来计算的式子
        self.flag = 0  # 判断是否计算完毕需要清空
        self.result.set(' ')
        self.equation.set('')
        self.equ_history = []
        self.res_history = []
        self.screen_history = []
        # 显示框 和 布局
        self.show_result_eq = Label(self.master, fg='black',font=('Arail', '16'), bd='2',textvariable=self.screen_equation, anchor='se')
        self.show_result = Label(self.master, fg='black',font=('Arail', '25'), bd='2',textvariable=self.result, anchor='se')
        self.show_result_eq.place(x='20', y='10', width='525', height='50')
        self.show_result.place(x='20', y='60', width='525', height='50')
        # 按钮 第1行
        self.button_cube_root = BTN(self.master, 'X^1/3', fun=lambda: self.getNum('**(1/3)'),args=('10', '150', '60', '40')) # x^(1/3)
        self.button_XY = BTN(self.master, 'X^y', fun=lambda: self.getNum('**'),args=('90', '150', '60', '40')) #todo 次方项如何开发  显示 x^
        self.button_left = BTN(self.master, '(', fun=lambda: self.getNum('('),args=('170','150','60','40'))
        self.button_right = BTN(self.master, ')', fun=lambda: self.getNum(')'),args=('250', '150', '60', '40'))
        self.button_c = BTN(self.master, 'C',  fun=self.clear,args=('330', '150','60','40'),fg='red')
        self.button_back = BTN(self.master, 'Back', fun=self.back, args=('410', '150', '60', '40'))
        self.button_division = BTN(self.master, text='÷',  fun=lambda: self.getNum('÷'),args=('490', '150', '60', '40'),fg='red')
        # 按钮 第2行
        self.button_sqrt = BTN(self.master, 'X^1/2', fun=lambda: self.getNum('**0.5'),args=('10', '205', '60', '40'))  # 显示 x^(1/2)
        self.button_e_x = BTN(self.master, 'e^x', fun=lambda: self.getNum('e**'),args=('90', '205', '60', '40'))  #todo e^ 显示
        self.button_10mi = BTN(self.master, '10^x', fun=lambda: self.getNum('10**'),args=('170', '205', '60', '40'))
        self.button_7 = BTN(self.master, '7', fun=lambda: self.getNum('7'),args=('250', '205', '60', '40'))
        self.button_8 = BTN(self.master, '8', fun=lambda: self.getNum('8'), args=('330', '205', '60', '40'))
        self.button_9 = BTN(self.master, '9', fun=lambda: self.getNum('9'), args=('410', '205', '60', '40'))
        self.button_mutil = BTN(self.master, text='x', fun=lambda: self.getNum('*'),args=('490', '205', '60', '40'),fg='red')

        # 按钮 第3行
        self.button_square = BTN(self.master, 'X^2', fun=lambda: self.getNum('**2'),args=('10', '260', '60', '40'))
        self.button_E = BTN(self.master, 'E', fun=lambda: self.getNum('e'),args=('90', '260', '60', '40'))
        self.button_log = BTN(self.master, 'log',  fun=lambda: self.getNum('log'), args=('170', '260', '60', '40'))
        self.button_4 = BTN(self.master, '4', fun=lambda: self.getNum('4'),args=('250', '260', '60', '40'))
        self.button_5 = BTN(self.master, '5', fun=lambda: self.getNum('5'),args=('330', '260', '60', '40'))
        self.button_6 = BTN(self.master, '6', fun=lambda: self.getNum('6'),args=('410', '260', '60', '40'))
        self.button_sub = BTN(self.master, text='-', fun=lambda: self.getNum('-'),args=('490', '260', '60', '40'),fg='red')

        # 按钮 第4行
        self.button_cube = BTN(self.master, 'X^3', fun=lambda: self.getNum('**3'),args=('10', '315', '60', '40'))
        self.button_pi = BTN(self.master, 'Π', fun=lambda: self.getNum('pi'),args=('90', '315', '60', '40'))
        self.button_ln = BTN(self.master, 'ln', fun=lambda: self.getNum('log'),args=('170', '315', '60', '40'))
        self.button_1 = BTN(self.master, '1', fun=lambda: self.getNum('1'),args=('250', '315', '60', '40'))
        self.button_2 = BTN(self.master, '2', fun=lambda: self.getNum('2'),args=('330', '315', '60', '40'))
        self.button_3 = BTN(self.master, '3', fun=lambda: self.getNum('3'),args=('410', '315', '60', '40'))
        self.button_add = BTN(self.master, text='+', fun=lambda: self.getNum('+'),args=('490', '315', '60', '40'),fg='red')

        # 按钮 第5行
        self.button_sin = BTN(self.master, 'sin', fun=lambda: self.getNum('sin'),args=('10', '370', '60', '40'))
        self.button_cos = BTN(self.master, 'cos', fun=lambda: self.getNum('cos'),args=('90', '370', '60', '40'))
        self.button_tan = BTN(self.master, 'tan', fun=lambda: self.getNum('tan'),args=('170', '370', '60', '40'))
        self.button_ce = BTN(self.master, 'CE', fun=self.get_history, args=('250', '370', '60', '40'),fg='red')
        self.button_0 = BTN(self.master, '0', fun=lambda: self.getNum('0'),args=('330', '370', '60', '40'))
        self.button_point = BTN(self.master, '.', fun=lambda: self.getNum('.'),args=('410', '370', '60', '40'))
        self.button_equ = BTN(self.master, text='=', fun=self.run, args=('490', '370', '60', '40'),fg='red')

    def back(self):
        self.flag = 0
        temp_equ = self.equation.get()
        temp_screen = self.screen_equation.get()
        self.screen_equation.set(temp_screen[:-1])
        if temp_equ[-2:] == '**':
            self.equation.set(temp_equ[:-2])
            self.screen_equation.set(temp_screen[:-1])
        elif temp_equ[-3:] == 'log':
            self.equation.set(temp_equ[:-3])
            self.screen_equation.set(temp_screen[:-3])
        elif temp_equ[-2:] == 'pi':
            self.equation.set(temp_equ[:-2])
            self.screen_equation.set(temp_screen[:-1])
        elif temp_equ[-3:] == 'sin':
            self.equation.set(temp_equ[:-3])
            self.screen_equation.set(temp_screen[:-3])
        elif temp_equ[-3:] == 'cos':
            self.equation.set(temp_equ[:-3])
            self.screen_equation.set(temp_screen[:-3])
        elif temp_equ[-3:] == 'tan':
            self.equation.set(temp_equ[:-3])
            self.screen_equation.set(temp_screen[:-3])
        else:
            self.equation.set(temp_equ[:-1])  # 一个一个删
            self.screen_equation.set(temp_screen[:-1])

    def get_history(self):    # 查询历史记录和结果
        temp_equ = self.equation.get()
        pre_idx = self.equ_history.index(temp_equ)
        new_idx = (pre_idx - 1 + len(self.equ_history)) % len(self.equ_history) # 取出上一个计算式子和结果
        self.equation.set(self.equ_history[new_idx])
        self.result.set(self.res_history[new_idx])
        self.screen_equation.set(self.screen_history[new_idx])

    def getNum(self, num):
        if self.flag:
            self.screen_equation.set('')
            self.equation.set('0')
            self.result.set('')
            self.flag = 0
        temp_equ = self.equation.get()  # 输入算式
        temp_screen_equation = self.screen_equation.get()
        if temp_equ == '0' and (num not in ['.', '+', '-', '*', '÷']):  # 如果次输入为0，则紧跟则不能是数字，只是小数点或运算符
            temp_equ = ''
            temp_screen_equation = ''
        temp_screen_equation = temp_screen_equation + num
        temp_equ = temp_equ + num
        self.equation.set(temp_equ.replace('÷', '/'))
        self.screen_equation.set(temp_screen_equation.replace('**','^').replace('*','x').replace('pi','Π'))

    def clear(self):
        self.screen_equation.set('0')
        self.equation.set('0')
        self.result.set(' ')

    def run(self):
        temp_equ = self.equation.get()
        self.equ_history.append(temp_equ)
        temp_screen = self.screen_equation.get()
        self.screen_history.append(temp_screen)
        try:
            answer = '%.5f' % eval(temp_equ)  #  保留两位小数
            self.result.set(str(answer))
        except (ZeroDivisionError):  #  其他除0错误，或语法错误返回Error
            self.result.set(str('Error: 除零错误'))
        except NameError:
            self.result.set(str('Error: 请加上括号'))
        except SyntaxError:
            self.result.set(str('Error: 语法错误，请正确输入'))
        self.res_history.append(self.result.get())
        self.flag = 1
        return self.result.get()

class TestCalculator(unittest.TestCase):
    def test_1(self):
        Cal = Calculator(root)
        Cal.equation.set('16+3-5*2')
        result = Cal.run()
        self.assertEqual(result, '9.0')

    def test_2(self):
        Cal = Calculator(root)
        Cal.equation.set('2**3+3**2')
        result = Cal.run()
        self.assertEqual(result, '17.0')

    def test_3(self):
        Cal = Calculator(root)
        Cal.equation.set('2*log(e**2)-8**(1/3)+4**(1/2)')
        result = Cal.run()
        self.assertEqual(result, '4.0')

    def test_4(self):
        Cal = Calculator(root)
        Cal.equation.set('sin(pi/2)+cos(pi/2)+tan(pi/4)')
        result = Cal.run()
        self.assertEqual(result, '2.0')

    def test_5(self):
        Cal = Calculator(root)
        Cal.equation.set('(log10(10**5)-1)/2')
        result = Cal.run()
        self.assertEqual(result, '2.0')


# if __name__ == '__main__':
#     unittest.main()
if __name__ == "__main__":
    root = Tk()
    my_calculator = Calculator(root)
    root.mainloop()






