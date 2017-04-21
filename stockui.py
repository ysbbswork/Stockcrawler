#!/usr/bin/env python
#-*- coding:utf-8 -*-
import getstockvalue
import getallrank
import os
import sys


from tkinter import *
PythonVersion = 3
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
# import tkinter.filedialog as tkFileDialog
# import tkinter.simpledialog as tkSimpleDialog    #askstring()
photo = None


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('YO！STOCK！')
        self.master.geometry('1068x772')
        self.createWidgets()

    def createWidgets(self):
        global photo
        # photo = PhotoImage(file=r"E:\yscode\Stockcrawler\wait.gif")
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Frame2.TLabelframe', font=('宋体', 9))
        self.Frame2 = LabelFrame(
            self.top, text='个股查询', style='Frame2.TLabelframe')
        self.Frame2.place(relx=0.015, rely=0.539,
                          relwidth=0.982, relheight=0.457)

        self.style.configure('Frame1.TLabelframe', font=('宋体', 9))
        self.Frame1 = LabelFrame(
            self.top, text='选股分类', style='Frame1.TLabelframe')
        self.Frame1.place(relx=0.015, rely=0.052,
                          relwidth=0.982, relheight=0.488)

        self.style.configure('Label1.TLabel', anchor='w', font=('宋体', 22))
        self.Label1 = Label(self.top, text='YO！Stock!——YS',
                            style='Label1.TLabel')
        self.Label1.place(relx=0.382, rely=0.01,
                          relwidth=0.255, relheight=0.048)

        self.Picture1 = Canvas(self.Frame2, bg='#FFFFFF')
        self.Picture1.place(relx=0.008, rely=0.01,
                            relwidth=0.512, relheight=0.87)

        # self.Picture1.create_image(-25, 0, image=photo, anchor=NW)
        self.style.configure('Command1.TButton', font=('宋体', 9))
        self.Command1 = Button(
            self.Frame2, text='查询', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.541, rely=0.907,
                            relwidth=0.115, relheight=0.071)
        self.style.configure('Command2.TButton', font=('宋体', 9))
        self.Command2 = Button(
            self.Frame2, text='清空', command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0.750, rely=0.907,
                            relwidth=0.115, relheight=0.071)

        self.Text3Var = StringVar(value='')
        self.Text3 = Entry(
            self.Frame2, textvariable=self.Text3Var, font=('宋体', 9))
        self.Text3.place(relx=0.32, rely=0.907,
                         relwidth=0.207, relheight=0.071)

        self.Text2Font = Font(font=('宋体', 9))
        self.Text2 = Text(self.Frame2, font=self.Text2Font)
        self.Text2.place(relx=0.526, rely=0.045,
                         relwidth=0.459, relheight=0.819)

        self.style.configure('Label3.TLabel', anchor='w', font=('宋体', 9))
        self.Label3 = Label(self.Frame2, text='股票代码：', style='Label3.TLabel')
        self.Label3.place(relx=0.259, rely=0.929,
                          relwidth=0.057, relheight=0.065)

        self.style.configure('Line3.TSeparator', background='#000000')
        self.Line3 = Separator(
            self.Frame2, orient='horizontal', style='Line3.TSeparator')
        self.Line3.place(relx=0.008, rely=0.884,
                         relwidth=0.976, relheight=0.0028)

        self.Text1Font = Font(font=('宋体', 9))
        self.Text1 = Text(self.Frame1, font=self.Text1Font)
        self.Text1.place(relx=0.191, rely=0.042,
                         relwidth=0.794, relheight=0.936)
        self.v = IntVar()
        self.v.set(1)
        self.style.configure('Option9.TRadiobutton', font=('宋体', 9))
        self.Option9 = Radiobutton(
            self.Frame1, text='新股涨幅TOP', command=self.Optcommand9, variable=self.v, value=9, style='Option9.TRadiobutton')
        self.Option9.place(relx=0.023, rely=0.86,
                           relwidth=0.131, relheight=0.088)

        self.style.configure('Option8.TRadiobutton', font=('宋体', 9))
        self.Option8 = Radiobutton(
            self.Frame1, text='创业板涨幅TOP', command=self.Optcommand8, variable=self.v, value=8, style='Option8.TRadiobutton')
        self.Option8.place(relx=0.023, rely=0.76,
                           relwidth=0.131, relheight=0.088)

        self.style.configure('Option7.TRadiobutton', font=('宋体', 9))
        self.Option7 = Radiobutton(
            self.Frame1, text='中小板涨幅TOP', command=self.Optcommand7, variable=self.v, value=7, style='Option7.TRadiobutton')
        self.Option7.place(relx=0.023, rely=0.66,
                           relwidth=0.131, relheight=0.088)

        self.style.configure('Option6.TRadiobutton', font=('宋体', 9))
        self.Option6 = Radiobutton(
            self.Frame1, text='深市B股涨幅TOP', command=self.Optcommand6, variable=self.v, value=6, style='Option6.TRadiobutton')
        self.Option6.place(relx=0.023, rely=0.56,
                           relwidth=0.131, relheight=0.088)

        self.style.configure('Option5.TRadiobutton', font=('宋体', 9))
        self.Option5 = Radiobutton(
            self.Frame1, text='沪市B股涨幅TOP', variable=self.v, command=self.Optcommand5, value=5, style='Option5.TRadiobutton')
        self.Option5.place(relx=0.023, rely=0.46,
                           relwidth=0.131, relheight=0.088)

        self.style.configure('Option4.TRadiobutton', font=('宋体', 9))
        self.Option4 = Radiobutton(
            self.Frame1, text='深市A股涨幅TOP', variable=self.v, command=self.Optcommand4, value=4, style='Option4.TRadiobutton')
        self.Option4.place(relx=0.023, rely=0.36,
                           relwidth=0.131, relheight=0.088)

        self.style.configure('Option3.TRadiobutton', font=('宋体', 9))
        self.Option3 = Radiobutton(
            self.Frame1, text='沪市A股涨幅TOP', variable=self.v, command=self.Optcommand3, value=3, style='Option3.TRadiobutton')
        self.Option3.place(relx=0.023, rely=0.26,
                           relwidth=0.131, relheight=0.088)

        self.style.configure('Option2.TRadiobutton', font=('宋体', 9))
        self.Option2 = Radiobutton(
            self.Frame1, text='B股市场涨幅TOP', variable=self.v, command=self.Optcommand2, value=2, style='Option2.TRadiobutton')
        self.Option2.place(relx=0.023, rely=0.16,
                           relwidth=0.131, relheight=0.088)

        self.style.configure('Option1.TRadiobutton', font=('宋体', 9))
        self.Option1 = Radiobutton(
            self.Frame1, text='A股市场涨幅TOP', variable=self.v, command=self.Optcommand1, value=1, style='Option1.TRadiobutton')
        self.Option1.place(relx=0.023, rely=0.060,
                           relwidth=0.131, relheight=0.088)

        self.style.configure('Line1.TSeparator', background='#000000')
        self.Line1 = Separator(
            self.Frame1, orient='vertical', style='Line1.TSeparator')
        self.Line1.place(relx=0.175, rely=0.042,
                         relwidth=0.001, relheight=0.934)


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        global photo
        # self.Text1.insert(INSERT, self.v.get())
        # self.Text1.insert(INSERT, self.Text3.get())
        # self.Text2.insert(
        #     END, stockcrawler.getit(self.Text3.get()))
        if str(self.Text3.get()).isdigit():
            self.Text2.insert(
                END, getstockvalue.getstockvalue(self.Text3.get()))
            getstockvalue.getgif(self.Text3.get())
            while True:
                breakyoo = 1
                if os.path.exists(r"{0}.gif".format(self.Text3.get())) == True:
                    photo = PhotoImage(file=r"{0}.gif".format(self.Text3.get()))
                    self.Picture1.create_image(-20, 0, image=photo, anchor=NW)
                    break
                else:

                    if breakyoo >= 5:
                        break
                    else:
                        photo = PhotoImage(file=r"wait.gif")
                        self.Picture1.create_image(-20, 0, image=photo, anchor=NW)
                        breakyoo += 1
                        continue
        else:
            self.Text2.insert(
                END, "please input a stocknumber!\n")

        # except:

    def Command2_Cmd(self, event=None):
        self.Text2.delete(0.0, END)

    def Optcommand9(self):
        self.Text1.delete(0.0, END)
        self.Text1.insert(
            END, getallrank.getranknew())

    def Optcommand8(self):
        self.Text1.delete(0.0, END)
        self.Text1.insert(
            END, getallrank.getrankcyb())

    def Optcommand7(self):
        self.Text1.delete(0.0, END)
        self.Text1.insert(
            END, getallrank.getrankzxb())

    def Optcommand6(self):
        self.Text1.delete(0.0, END)
        self.Text1.insert(
            END, getallrank.getranksb())

    def Optcommand5(self):
        self.Text1.delete(0.0, END)
        self.Text1.insert(
            END, getallrank.getrankhb())

    def Optcommand4(self):
        self.Text1.delete(0.0, END)
        self.Text1.insert(
            END, getallrank.getranksa())

    def Optcommand3(self):
        self.Text1.delete(0.0, END)
        self.Text1.insert(
            END, getallrank.getrankha())

    def Optcommand2(self):
        self.Text1.delete(0.0, END)
        self.Text1.insert(
            END, getallrank.getrankb())

    def Optcommand1(self):
        self.Text1.delete(0.0, END)
        self.Text1.insert(
            END, getallrank.getranka())


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try:
        top.destroy()
    except:
        pass

      # # TODO, Please finish the function here!
      # photo = PhotoImage(file=r"E:\yscode\Stockcrawler\stockgif.gif")
      # self.Text1.insert(INSERT, "aaaaaa\nbbbb\nccc\n")
      # self.Text1.image_create(END, image=photo)
      # # self.Frame3.pack_forget()
