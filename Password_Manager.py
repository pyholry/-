import tkinter as tk
import tkinter.messagebox
import time

global file_name

def save_data():
    ##保存数据
    try:
        ##获取输入框的信息
        user = get_user.get()
        user_name = get_user_name.get()
        password = get_password.get()

        file_name = user + "_data.txt"#定义文件名
        #print(file_name)

        with open(file_name,'a') as f:
            f.write("账户名称：" + user + "\n")
            f.write("用户名/账号：" + user_name + "\n")
            f.write("密码：" + password + "\n")
            result_ok = "保存成功!\n"
            print(result_ok)
            t.insert('end',result_ok + "\n")#在信息框输出
    except:
        error_1 = "数据写入本地时遇到错误...\n请检查输入或咨询开发者解决\n"
        print(error_1)
        t.insert('end',error_1 + "\n")

def read_data():
    ##输出保存的数据
    try:
        #获取输入框的信息
        user = get_user.get()

        file_name = user + "_data.txt"#定义文件名

        with open(file_name) as r:
            contents = r.read()
            print(contents + "\n")
            t.insert('end',contents + "\n")#在信息框输出
    except:
        error_2 = "输出时遇到错误...\n请检查输入或咨询开发者解决"
        print(error_2)
        t.insert('end',error_2)

print("这是一个用户名与密码管理的程序"
      "\n你是否经常忘记密码？"
      "这个程序帮你储存你的用户名密码，"
      "使你不用再因为为忘记密码而发愁")

window = tk.Tk()
window.title('账户密码管理程序' + time.ctime())
window.geometry('500x350')

l = tk.Label(window,text='账户密码管理程序',width=40,font=('Arial', 12))
l.pack()

l_2 = tk.Label(window,text="使用说明：如果要储存用户名与密码，在下面三个输入框分别输入"
                           "\n账户名称、用户名或账号、密码，然后点击储存键；"
                           "\n如果要查询用户名与密码，则只需要在第一个输入框输入账户名称，点击查询键。",width=60,font=('Arial', 10))
l_2.pack()

get_user = tk.Entry(window,show=None,width=40)
get_user.pack()

get_user_name = tk.Entry(window,show=None,width=40)
get_user_name.pack()

get_password = tk.Entry(window,show=None,width=40)
get_password.pack()

b_1 = tk.Button(window,text='储存',width=10,height=1,command=save_data)
b_1.pack()

b_2 = tk.Button(window,text='查询',width=10,height=1,command=read_data)
b_2.pack()

l_3 = tk.Label(window,text='下面是输出结果',width=40,font=('Arial', 12))
l_3.pack()

t = tk.Text(window,width=50,height=4)
t.pack()

l_4 = tk.Label(window,text='程序已开源，源码在github上:查找'
                           '\n开发者秉承绝不远程连接服务器窃取用户信息的原则',width=60)
l_4.pack()

l_5 = tk.Label(window,text='有疑惑联系q2485520492',width=40,font=('Arial', 12))
l_5.pack()

tkinter.messagebox.showinfo(title='说明', message="这是一个用户名与密码管理的程序。"
                                                "你是否经常忘记密码？"
                                                "这个程序帮你储存你的用户名密码，使你不用再为忘记密码而发愁"
                                                "\n本程序由q2485520492（紫狐）开发")

window.mainloop()







