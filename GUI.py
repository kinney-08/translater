import tkinter
import json
import sys

import translate

class GUI_class:
    '''图形界面管理类'''
    def __init__(self):
        self.sitting = json.dumps({})
        with open(sys.path[0] + "/sittings.json") as sittings:
            self.sitting = json.load(sittings) #加载设置
        
        self.window = tkinter.Tk()
        self.window.title(self.sitting["title"])
        self.window.geometry(f"{self.sitting['size'][0]}x{self.sitting['size'][1]}") #初始化窗口

        self._output_box_data = tkinter.StringVar()

        self.input_box = tkinter.Entry(self.window, width = self.sitting["input_box"]["width"], #设置输入框
            font = self.sitting["input_box"]["font"])

        self.output_box = tkinter.Label(self.window, textvariable=self._output_box_data, 
            width = self.sitting["output_box"]["width"], font = self.sitting["output_box"]["font"]) #设置输出框

        self.trans_button = tkinter.Button(self.window, command = self.trans,
            width = self.sitting["trans_button"]["width"], height = self.sitting["trans_button"]["height"],
            font = self.sitting["input_box"]["font"], text = self.sitting["trans_button"]["text"]) #设置翻译按钮

        self.input_box.pack()
        self.output_box.pack()
        self.trans_button.pack()
        self.trans = translate.translate_class() #全部加载

    def trans(self):
        """进行翻译"""
        try:
            ans = self.trans.translate(str(self.input_box.get()))
        except translate.NetworkError as w:
            ans = w.why
        except translate.RequestError as w:
            ans = w.why
        self._output_box_data.set(ans) 
    

    def run(self):
        self.window.mainloop()

    
        

if __name__ == "__main__":
    a = GUI_class()
    a.run()