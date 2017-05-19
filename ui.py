#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
import getstockvalue
import getallrank
import selectinsql
import getallstock
import pandasuse
photo = None


class Application_ui(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('yo!stock——ys')
        self.master.geometry('754x433')
        self.master.resizable(0, 0)
        self.createWidgets()

    def createWidgets(self):
        global photo
        self.v = IntVar()
        self.v.set(1)
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.TabStrip1 = Notebook(self.top)
        self.TabStrip1.place(relx=0., rely=0., relwidth=0.999, relheight=1.)

        self.TabStrip1__Tab1 = Frame(self.TabStrip1)
        self.Text3Font = Font(font=('宋体', 9))
        self.Text3 = Text(self.TabStrip1__Tab1, font=self.Text3Font)
        self.Text3.place(relx=0.695, rely=0.039,
                         relwidth=0.273, relheight=0.746)
        self.style.configure('Command3.TButton', font=('宋体', 9))
        self.Command3 = Button(self.TabStrip1__Tab1, text='清除',
                               command=self.Command3_Cmd, style='Command3.TButton')
        self.Command3.place(relx=0.651, rely=0.861,
                            relwidth=0.186, relheight=0.061)
        self.Picture1 = Canvas(self.TabStrip1__Tab1, bg='#FFFFFF')
        self.Picture1.place(relx=0.011, rely=0.039,
                            relwidth=0.674, relheight=0.726)
        self.style.configure('Command1.TButton', font=('宋体', 9))
        self.Command1 = Button(self.TabStrip1__Tab1, text='查询',
                               command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.423, rely=0.861,
                            relwidth=0.186, relheight=0.061)
        self.Text1Var = StringVar(value='')
        self.Text1 = Entry(self.TabStrip1__Tab1,
                           textvariable=self.Text1Var, font=('宋体', 9))
        self.Text1.place(relx=0.141, rely=0.861,
                         relwidth=0.251, relheight=0.061)
        self.style.configure('Label14.TLabel', anchor='w', font=('宋体', 9))
        self.Label14 = Label(self.TabStrip1__Tab1,
                             text='股票代码：', style='Label14.TLabel')
        self.Label14.place(relx=0.035, rely=0.870,
                           relwidth=0.081, relheight=0.055)
        self.TabStrip1.add(self.TabStrip1__Tab1, text='在线个股查询')

        self.TabStrip1__Tab2 = Frame(self.TabStrip1)
        self.style.configure('Option7.TRadiobutton', font=('宋体', 9))
        self.Option7 = Radiobutton(
            self.TabStrip1__Tab2, text='中小板涨幅TOP', command=self.Optcommand14, variable=self.v, value=12, style='Option7.TRadiobutton')
        self.Option7.place(relx=0.011, rely=0.509,
                           relwidth=0.142, relheight=0.042)
        self.style.configure('Option6.TRadiobutton', font=('宋体', 9))
        self.Option6 = Radiobutton(
            self.TabStrip1__Tab2, text='深市B股涨幅TOP', command=self.Optcommand13, variable=self.v, value=11, style='Option6.TRadiobutton')
        self.Option6.place(relx=0.011, rely=0.43,
                           relwidth=0.142, relheight=0.042)
        self.style.configure('Option5.TRadiobutton', font=('宋体', 9))
        self.Option5 = Radiobutton(
            self.TabStrip1__Tab2, text='沪市B股涨幅TOP', command=self.Optcommand12, variable=self.v, value=10, style='Option5.TRadiobutton')
        self.Option5.place(relx=0.011, rely=0.352,
                           relwidth=0.142, relheight=0.042)
        self.style.configure('Option4.TRadiobutton', font=('宋体', 9))
        self.Option4 = Radiobutton(
            self.TabStrip1__Tab2, text='深市A股涨幅TOP', command=self.Optcommand11, variable=self.v, value=9, style='Option4.TRadiobutton')
        self.Option4.place(relx=0.011, rely=0.274,
                           relwidth=0.142, relheight=0.042)
        self.style.configure('Option3.TRadiobutton', font=('宋体', 9))
        self.Option3 = Radiobutton(
            self.TabStrip1__Tab2, text='沪市A股涨幅TOP', command=self.Optcommand10, variable=self.v, value=8, style='Option3.TRadiobutton')
        self.Option3.place(relx=0.011, rely=0.196,
                           relwidth=0.142, relheight=0.042)
        self.style.configure('Option2.TRadiobutton', font=('宋体', 9))
        self.Option2 = Radiobutton(
            self.TabStrip1__Tab2, text='B股市场涨幅TOP', command=self.Optcommand9, variable=self.v, value=7, style='Option2.TRadiobutton')
        self.Option2.place(relx=0.011, rely=0.117,
                           relwidth=0.142, relheight=0.061)
        self.style.configure('Option1.TRadiobutton', font=('宋体', 9))
        self.Option1 = Radiobutton(
            self.TabStrip1__Tab2, text='A股市场涨幅TOP', command=self.Optcommand8, variable=self.v, value=6, style='Option1.TRadiobutton')
        self.Option1.place(relx=0.011, rely=0.059,
                           relwidth=0.142, relheight=0.042)
        self.Text2Font = Font(font=('宋体', 9))
        self.Text2 = Text(self.TabStrip1__Tab2, font=self.Text2Font)
        self.Text2.place(relx=0.195, rely=0.039,
                         relwidth=0.794, relheight=0.902)
        self.style.configure('Line3.TSeparator', background='#000000')
        self.Line3 = Separator(self.TabStrip1__Tab2,
                               orient='vertical', style='Line3.TSeparator')
        self.Line3.place(relx=0.174, rely=0.039,
                         relwidth=0.0014, relheight=0.919)
        self.TabStrip1.add(self.TabStrip1__Tab2, text='在线TOP榜单')

        self.TabStrip1__Tab3 = Frame(self.TabStrip1)
        self.Text6Font = Font(font=('宋体', 9))
        self.Text6 = Text(self.TabStrip1__Tab3, font=self.Text6Font)
        self.Text6.place(relx=0.310, rely=0.060,
                         relwidth=0.7, relheight=0.901)
        self.style.configure('Command2.TButton', font=('宋体', 9))
        self.Command2 = Button(self.TabStrip1__Tab3, text='查询',
                               command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0.075, rely=0.352,
                            relwidth=0.164, relheight=0.1)
        self.Text5Var = StringVar(value='')
        self.Text5 = Entry(self.TabStrip1__Tab3,
                           textvariable=self.Text5Var, font=('宋体', 9))
        self.Text5.place(relx=0.119, rely=0.215,
                         relwidth=0.15, relheight=0.044)
        self.Text4Var = StringVar(value='')
        self.Text4 = Entry(self.TabStrip1__Tab3,
                           textvariable=self.Text4Var, font=('宋体', 9))
        self.Text4.place(relx=0.119, rely=0.059,
                         relwidth=0.15, relheight=0.044)
        self.style.configure('Label6.TLabel', anchor='w', font=('宋体', 9))
        self.Label6 = Label(
            self.TabStrip1__Tab3, text='查询日期为历史爬取日期。例:20170505', style='Label6.TLabel')
        self.Label6.place(relx=0.01, rely=0.7,
                          relwidth=0.30, relheight=0.068)
        self.Label66 = Label(
            self.TabStrip1__Tab3, text='查询结果与数据库完整性有关', style='Label6.TLabel')
        self.Label66.place(relx=0.05, rely=0.8,
                           relwidth=0.25, relheight=0.068)
        self.style.configure('Label666.TLabel', anchor='w', font=('宋体', 9))
        self.Label666 = Label(
            self.TabStrip1__Tab3, text="|股票代码 |股票简称 | 最新价 | 涨跌幅 | 涨跌额 | 成交量(手) | 成交额(万元) | 换手率 |", style='Label666.TLabel')
        self.Label666.place(relx=0.310, rely=0.001,
                            relwidth=0.7, relheight=0.048)

        self.style.configure('Label5.TLabel', anchor='w', font=('宋体', 9))
        self.Label5 = Label(self.TabStrip1__Tab3,
                            text='股票代码：', style='Label5.TLabel')
        self.Label5.place(relx=0.022, rely=0.215,
                          relwidth=0.081, relheight=0.045)
        self.style.configure('Label1.TLabel', anchor='w', font=('宋体', 9))
        self.Label1 = Label(self.TabStrip1__Tab3,
                            text='查询日期：', style='Label1.TLabel')
        self.Label1.place(relx=0.022, rely=0.059,
                          relwidth=0.081, relheight=0.045)
        self.style.configure('Command6.TButton', font=('宋体', 9))
        self.Command6 = Button(self.TabStrip1__Tab3, text='清除',
                               command=self.Command6_Cmd, style='Command6.TButton')
        self.Command6.place(relx=0.075, rely=0.548,
                            relwidth=0.164, relheight=0.1)
        self.TabStrip1.add(self.TabStrip1__Tab3, text='数据库个股查询')

        self.TabStrip1__Tab4 = Frame(self.TabStrip1)
        self.style.configure('Option13.TRadiobutton', font=('宋体', 9))
        self.Option13 = Radiobutton(
            self.TabStrip1__Tab4, text='中小板', variable=self.v, value=15, style='Option13.TRadiobutton')
        self.Option13.place(relx=0.695, rely=0.078,
                            relwidth=0.099, relheight=0.042)
        self.style.configure('Option16.TRadiobutton', font=('宋体', 9))
        self.Option13 = Radiobutton(
            self.TabStrip1__Tab4, text='其他', variable=self.v, value=16, style='Option13.TRadiobutton')
        self.Option13.place(relx=0.810, rely=0.078,
                            relwidth=0.099, relheight=0.042)

        self.style.configure('Command4.TButton', font=('宋体', 9))
        self.Command4 = Button(self.TabStrip1__Tab4, text='查询',
                               command=self.Command4_Cmd, style='Command4.TButton')
        self.Command4.place(relx=0.054, rely=0.665,
                            relwidth=0.186, relheight=0.061)
        self.Text11Font = Font(font=('宋体', 9))
        self.Text11 = Text(self.TabStrip1__Tab4, font=self.Text11Font)
        self.Text11.place(relx=0.271, rely=0.2,
                          relwidth=0.718, relheight=0.780)
        self.style.configure('Frame1.TLabelframe', font=('宋体', 9))
        self.Frame1 = LabelFrame(self.TabStrip1__Tab4,
                                 text='自定义选项', style='Frame1.TLabelframe')
        self.Frame1.place(relx=0.033, rely=0.156,
                          relwidth=0.229, relheight=0.452)
        self.Text10Var = StringVar(value='')
        self.Text10 = Entry(self.Frame1,
                            textvariable=self.Text10Var, font=('宋体', 9))
        self.Text10.place(relx=0.568, rely=0.562,
                          relwidth=0.29, relheight=0.097)
        self.Text9Var = StringVar()
        self.Text9 = Entry(self.Frame1,
                           textvariable=self.Text9Var, font=('宋体', 9))
        self.Text9.place(relx=0.568, rely=0.389,
                         relwidth=0.29, relheight=0.097)
        self.Text8Var = StringVar()
        self.Text8 = Entry(self.Frame1,
                           textvariable=self.Text8Var, font=('宋体', 9))
        self.Text8.place(relx=0.568, rely=0.216,
                         relwidth=0.29, relheight=0.097)
        self.style.configure('Label11.TLabel', anchor='w', font=('宋体', 9))
        self.Label11 = Label(self.Frame1, text='成交额', style='Label11.TLabel')
        self.Label11.place(relx=0.095, rely=0.562,
                           relwidth=0.29, relheight=0.092)
        self.style.configure('Label10.TLabel', anchor='w', font=('宋体', 9))
        self.Label10 = Label(self.Frame1, text='成交量', style='Label10.TLabel')
        self.Label10.place(relx=0.095, rely=0.389,
                           relwidth=0.243, relheight=0.092)
        self.style.configure('Label9.TLabel', anchor='w', font=('宋体', 9))
        self.Label9 = Label(self.Frame1, text='升降序1/0', style='Label9.TLabel')
        self.Label9.place(relx=0.568, rely=0.056,
                          relwidth=0.35, relheight=0.1)
        self.style.configure('Line2.TSeparator', background='#000000')
        self.Line2 = Separator(
            self.Frame1, orient='horizontal', style='Line2.TSeparator')
        self.Line2.place(relx=0.047, rely=0.173,
                         relwidth=0.899, relheight=0.0054)
        self.style.configure('Line1.TSeparator', background='#000000')
        self.Line1 = Separator(
            self.Frame1, orient='vertical', style='Line1.TSeparator')
        self.Line1.place(relx=0.473, rely=0.086,
                         relwidth=0.0059, relheight=0.865)
        self.style.configure('Label8.TLabel', anchor='w', font=('宋体', 9))
        self.Label8 = Label(self.Frame1, text='关键词', style='Label8.TLabel')
        self.Label8.place(relx=0.095, rely=0.056,
                          relwidth=0.25, relheight=0.1)
        self.style.configure('Label7.TLabel', anchor='w', font=('宋体', 9))
        self.Label7 = Label(self.Frame1, text='股票价格', style='Label7.TLabel')
        self.Label7.place(relx=0.095, rely=0.216,
                          relwidth=0.337, relheight=0.092)
        self.style.configure('Option9.TRadiobutton', font=('宋体', 9))
        self.Option9 = Radiobutton(
            self.TabStrip1__Tab4, text='B股市场', variable=self.v, value=14, style='Option9.TRadiobutton')
        self.Option9.place(relx=0.554, rely=0.078,
                           relwidth=0.088, relheight=0.042)
        self.style.configure('Option8.TRadiobutton', font=('宋体', 9))
        self.Option8 = Radiobutton(
            self.TabStrip1__Tab4, text='A股市场', variable=self.v, value=13, style='Option8.TRadiobutton')
        self.Option8.place(relx=0.412, rely=0.078,
                           relwidth=0.11, relheight=0.042)
        self.Text7Var = StringVar(value='')
        self.Text7 = Entry(self.TabStrip1__Tab4,
                           textvariable=self.Text7Var, font=('宋体', 9))
        self.Text7.place(relx=0.141, rely=0.078,
                         relwidth=0.208, relheight=0.044)
        self.style.configure('Label2.TLabel', anchor='w', font=('宋体', 9))
        self.Label2 = Label(self.TabStrip1__Tab4,
                            text='数据库日期：', style='Label2.TLabel')
        self.Label2.place(relx=0.033, rely=0.078,
                          relwidth=0.098, relheight=0.045)
        self.style.configure('Label22.TLabel', anchor='w', font=('宋体', 9))
        self.Label22 = Label(self.TabStrip1__Tab4,
                             text='|股票代码|股票简称|最新价| 涨跌幅| 涨跌额 |成交量(手)|成交额|换手率|', style='Label2.TLabel')
        self.Label22.place(relx=0.3, rely=0.15,
                           relwidth=0.6, relheight=0.045)

        self.style.configure('Command7.TButton', font=('宋体', 9))
        self.Command7 = Button(self.TabStrip1__Tab4, text='清除',
                               command=self.Command7_Cmd, style='Command7.TButton')
        self.Command7.place(relx=0.054, rely=0.763,
                            relwidth=0.186, relheight=0.061)
        self.TabStrip1.add(self.TabStrip1__Tab4, text='自定义排行查询')

        self.TabStrip1__Tab5 = Frame(self.TabStrip1)
        self.style.configure('Command5.TButton', font=('宋体', 9))
        self.Command5 = Button(self.TabStrip1__Tab5, text='爬起来',
                               command=self.Command5_Cmd, style='Command5.TButton')
        self.Command5.place(relx=0.315, rely=0.45,
                            relwidth=0.327, relheight=0.081)
        self.Text12Var = StringVar(value='')
        self.Text12 = Entry(self.TabStrip1__Tab5,
                            textvariable=self.Text12Var, font=('宋体', 9))
        self.Text12.place(relx=0.293, rely=0.274,
                          relwidth=0.598, relheight=0.044)
        self.style.configure('Option15.TRadiobutton', font=('宋体', 9))
        self.Option15 = Radiobutton(
            self.TabStrip1__Tab5, text='爬指定网页', variable=self.v, value=5, style='Option15.TRadiobutton')
        self.Option15.place(relx=0.087, rely=0.274,
                            relwidth=0.121, relheight=0.042)
        self.style.configure('Option14.TRadiobutton', font=('宋体', 9))
        self.Option14 = Radiobutton(
            self.TabStrip1__Tab5, text='中小板', variable=self.v, value=3, style='Option14.TRadiobutton')
        self.Option14.place(relx=0.347, rely=0.117,
                            relwidth=0.099, relheight=0.061)
        self.style.configure('Option12.TRadiobutton', font=('宋体', 9))
        self.Option12 = Radiobutton(
            self.TabStrip1__Tab5, text='全部都爬', variable=self.v, value=4, style='Option12.TRadiobutton')
        self.Option12.place(relx=0.456, rely=0.117,
                            relwidth=0.11, relheight=0.061)
        self.style.configure('Option11.TRadiobutton', font=('宋体', 9))
        self.Option11 = Radiobutton(
            self.TabStrip1__Tab5, text='只爬B股', variable=self.v, value=2, style='Option11.TRadiobutton')
        self.Option11.place(relx=0.228, rely=0.117,
                            relwidth=0.121, relheight=0.061)
        self.style.configure('Option10.TRadiobutton', font=('宋体', 9))
        self.Option10 = Radiobutton(
            self.TabStrip1__Tab5, text='只爬A股', variable=self.v, value=1, style='Option10.TRadiobutton')
        self.Option10.place(relx=0.087, rely=0.117,
                            relwidth=0.099, relheight=0.061)
        self.style.configure('Label3.TLabel', anchor='w', font=('宋体', 9))
        self.Label3 = Label(self.TabStrip1__Tab5,
                            text='URL：', style='Label3.TLabel')
        self.Label3.place(relx=0.228, rely=0.277,
                          relwidth=0.056, relheight=0.042)
        self.style.configure('Label15.TLabel', anchor='w',
                             foreground='#3399FF', font=('宋体', 9))
        self.Label15 = Label(
            self.TabStrip1__Tab5, text='你可以定制本次爬虫任务，选择爬取股票分类市场或者全部都爬，爬取速度和要爬取的内容成正相关', style='Label15.TLabel')
        self.Label15.place(relx=0.054, rely=0.059,
                           relwidth=0.75, relheight=0.042)
        self.Text13Var = StringVar()
        self.Text13 = Entry(self.TabStrip1__Tab5,
                            textvariable=self.Text13Var, font=('宋体', 9))
        self.Text13.place(relx=0.174, rely=0.587,
                          relwidth=0.729, relheight=0.061)
        self.style.configure('Label12.TLabel', anchor='w', font=('宋体', 9))
        self.Label12 = Label(
            self.TabStrip1__Tab5, text='爬取过程可能会占用系统资源，请勿做其它操作，当爬取完毕，会显示：已完成本次爬取工作！', style='Label12.TLabel')
        self.Label12.place(relx=0.119, rely=0.743,
                           relwidth=0.718, relheight=0.042)
        self.style.configure('Label13.TLabel', anchor='w', font=('宋体', 9))
        self.Label13 = Label(
            self.TabStrip1__Tab5, text='指定网页为证券之星股票市场网页，可以爬取A/B/中小板之外的股票信息并存入数据库', style='Label13.TLabel')
        self.Label13.place(relx=0.109, rely=0.352,
                           relwidth=0.696, relheight=0.061)
        self.style.configure('Label16.TLabel', anchor='w', font=('宋体', 9))
        self.Label16 = Label(self.TabStrip1__Tab5,
                             text='返回信息：', style='Label16.TLabel')
        self.Label16.place(relx=0.076, rely=0.606,
                           relwidth=0.081, relheight=0.045)
        self.TabStrip1.add(self.TabStrip1__Tab5, text='爬虫设置')

        self.TabStrip1__Tab6 = Frame(self.TabStrip1)
        self.style.configure('Label4.TLabel', anchor='w', font=('宋体', 9))
        self.Label4 = Label(
            self.TabStrip1__Tab6, text='作者：ysbbs  blog:ysbbs.cf', style='Label4.TLabel')
        self.Label4.place(relx=0.065, rely=0.235,
                          relwidth=0.609, relheight=0.1)
        self.style.configure('Label17.TLabel', anchor='w', font=('宋体', 9))
        self.Label17 = Label(self.TabStrip1__Tab6,
                             text='联系方式：ysbbs@qq.com', style='Label17.TLabel')
        self.Label17.place(relx=0.065, rely=0.352,
                           relwidth=0.598, relheight=0.1)
        self.style.configure('Label18.TLabel', anchor='w', font=('宋体', 9))
        self.Label18 = Label(
            self.TabStrip1__Tab6, text='Yo!stock!——是一个中国股票爬虫程序，附带了一些小功能，结合了mysql数据库，使用Python3.5编写。', style='Label18.TLabel')
        self.Label18.place(relx=0.065, rely=0.059,
                           relwidth=0.815, relheight=0.12)
        self.TabStrip1.add(self.TabStrip1__Tab6, text='关于')
        photo = PhotoImage(file=r"wait.gif")
        self.Picture1.create_image(-28, 0, image=photo, anchor=NW)


class Application(Application_ui):

    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command3_Cmd(self, event=None):
        self.Text3.delete(0.0, END)

    def Command1_Cmd(self, event=None):
        global photo
        if str(self.Text1.get()).isdigit():
            self.Text3.insert(
                END, getstockvalue.getstockvalue(self.Text1.get()))
            getstockvalue.getgif(self.Text1.get())
            while True:
                breakyoo = 1
                if os.path.exists(r"{0}.gif".format(self.Text1.get())) == True:
                    photo = PhotoImage(
                        file=r"{0}.gif".format(self.Text1.get()))
                    self.Picture1.create_image(-20, 0, image=photo, anchor=NW)
                    break
                else:

                    if breakyoo >= 5:
                        break
                    else:
                        photo = PhotoImage(file=r"wait.gif")
                        self.Picture1.create_image(-20,
                                                   0, image=photo, anchor=NW)
                        breakyoo += 1
                        continue
        else:
            self.Text3.insert(
                END, "请输入一个股票代码！\n")

        # except:

    def Command2_Cmd(self, event=None):
        if str(self.Text5.get()).isdigit():
            self.Text6.insert(END, selectinsql.selectinsql(
                self.Text4.get(), self.Text5.get()))
        else:
            self.Text6.insert(
                END, "请输入一个股票代码!\n")

    def Command6_Cmd(self, event=None):
        self.Text6.delete(0.0, END)

    def Command4_Cmd(self, event=None):
        self.Text11.delete(0.0, END)
        which_mode = self.v.get()
        # print(which_mode)
        if which_mode == 13:
            data_choose = "a" + str(self.Text7.get())
        elif which_mode == 14:
            data_choose = "b" + str(self.Text7.get())
        elif which_mode == 15:
            data_choose = "zxb" + str(self.Text7.get())
        elif which_mode == 16:
            data_choose = "other" + str(self.Text7.get())
        else:
            self.Text11.insert(END, "请选择一个市场类型！")
            data_choose = "a" + str(self.Text7.get())
        self.Text11.insert(END, pandasuse.pandait(
            data_choose, self.Text8.get(), self.Text9.get(), self.Text10.get()))

    def Command7_Cmd(self, event=None):
        self.Text11.delete(0.0, END)

    def Command5_Cmd(self, event=None):
        which_mode = self.v.get()
        # print(which_mode)
        if which_mode == 1:
            self.Text13.insert(END, getallstock.getranka())
        elif which_mode == 2:
            self.Text13.insert(END, getallstock.getrankb())
        elif which_mode == 3:
            self.Text13.insert(END, getallstock.getrankzxb())
        elif which_mode == 4:
            self.Text13.insert(END, getallstock.getall())
        elif which_mode == 5:
            self.Text13.insert(
                END, getallstock.getstarstockurlstock(self.Text12.get()))

    def Optcommand8(self):  # 从8开始8~14为在线rank
        self.Text2.delete(0.0, END)
        self.Text2.insert(
            END, getallrank.getranka())

    def Optcommand9(self):
        self.Text2.delete(0.0, END)
        self.Text2.insert(
            END, getallrank.getrankb())

    def Optcommand10(self):
        self.Text2.delete(0.0, END)
        self.Text2.insert(
            END, getallrank.getrankha())

    def Optcommand11(self):
        self.Text2.delete(0.0, END)
        self.Text2.insert(
            END, getallrank.getranksa())

    def Optcommand12(self):
        self.Text2.delete(0.0, END)
        self.Text2.insert(
            END, getallrank.getrankhb())

    def Optcommand13(self):
        self.Text2.delete(0.0, END)
        self.Text2.insert(
            END, getallrank.getranksb())

    def Optcommand14(self):
        self.Text2.delete(0.0, END)
        self.Text2.insert(
            END, getallrank.getrankzxb())


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try:
        top.destroy()
    except:
        pass
