##解一元二次方程##
#一般式：a*x**2 + b*x + c = 0
#求根公式: x = (-b + (b**2 - 4*a*c)**0.5) / 2*a 或 x = (-b - (b**2 - 4*a*c)**0.5) / 2*a

import tkinter as tk
import time
global a,b,c
global x,x_1,x_2
global discriminant

def solve_equations():
    try:
        var_a = a_get.get()
        var_b = b_get.get()
        var_c = c_get.get()

        a = float(var_a)
        b = float(var_b)
        c = float(var_c)

        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            result_1 = "该方程无解\n"
            print(result_1)
            t.insert('end',result_1)

        elif discriminant == 0:
            print("该方程有两个相同的解")
            x = (-b + discriminant**0.5) / 2*a
            result_2 = "x1 = x2 = " + str(x) + "\n"
            print(result_2)
            t.insert('end', result_2)

        elif discriminant > 0:
            print("该方程有两个不同的解")
            x_1 = (-b + discriminant** 0.5) / 2 * a
            x_2 = (-b - discriminant** 0.5) / 2 * a
            result_3 = "x1 = " + str(x_1)  + " ,x2 = " + str(x_2) + "\n"
            print(result_3)
            t.insert('end',result_3)
    except:
        error_h = "请检查输入是否正确...\n"
        print(error_h)
        t.insert('end',error_h)

window = tk.Tk()
window.title('解一元二次方程' + time.ctime())
window.geometry('500x300')

l = tk.Label(window,text='解一元二次方程',width=40,font=('Arial', 12))
l.pack()

l_2 = tk.Label(window,text="在下面三个输入框依次输入一般式中a,b,c的值，点击开始键，输出相应的解",width=60,font=('Arial', 10))
l_2.pack()

a_get = tk.Entry(window,show=None,width=40)
a_get.pack()

b_get = tk.Entry(window,show=None,width=40)
b_get.pack()

c_get = tk.Entry(window,show=None,width=40)
c_get.pack()

b_1 = tk.Button(window,text='开始',width=10,height=1,command=solve_equations)
b_1.pack()

l_3 = tk.Label(window,text='下面是方程的根',width=40,font=('Arial', 12))
l_3.pack()

t = tk.Text(window,width=50,height=4)
t.pack()

l_4 = tk.Label(window,text='有疑惑联系q2485520492',width=40,font=('Arial', 12))
l_4.pack()

window.mainloop()











































