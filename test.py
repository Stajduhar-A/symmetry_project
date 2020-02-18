from kivy.app import App
import pandas as pd
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.graphics import *
import os
from kivy.core.window import Window
import random

class Experiment(FloatLayout):
    # Uncomment the line below to make the kivy window fullscreen. Do not necessarily recommend.
    # Window.fullscreen = True
    sym_ort = ['sym_ort/' + stim for stim in os.listdir("sym_ort/")]
    random.shuffle(sym_ort)
    asym_ort = ['asym_ort/' + stim for stim in os.listdir("asym_ort/")]
    random.shuffle(asym_ort)
    sym_per = ['sym_per/' + stim for stim in os.listdir("sym_per/")]
    random.shuffle(sym_per)
    asym_per = ['asym_per/' + stim for stim in os.listdir("asym_per/")]
    random.shuffle(asym_per)

    trial = 0

    image_x_0 = 55
    image_y_0 = 55
    image_x_1 = 55
    image_y_1 = 110
    image_x_2 = 55
    image_y_2 = 165
    image_x_3 = 55
    image_y_3 = 220
    image_x_4 = 55
    image_y_4 = 275
    image_x_5 = 55
    image_y_5 = 330
    image_x_6 = 55
    image_y_6 = 385
    image_x_7 = 55
    image_y_7 = 440

    image_0 = Image(source=sym_ort[trial], id='img0', size=(100, 100))
    scatter_0 = Scatter(do_rotation=False, do_scale=False, auto_bring_to_front=False)
    scatter_0.set_center_x(image_x_0 + 18)
    scatter_0.set_center_y(image_y_0 + 23)
    scatter_0.add_widget(image_0)

    image_1 = Image(source=asym_ort[trial], id='img1', size=(100, 100))
    scatter_1 = Scatter(do_rotation=False, do_scale=False, auto_bring_to_front=False)
    scatter_1.set_center_x(image_x_1 + 18)
    scatter_1.set_center_y(image_y_1 + 23)
    scatter_1.add_widget(image_1)

    image_2 = Image(source=sym_per[trial], id='img2', size=(100, 100))
    scatter_2 = Scatter(do_rotation=False, do_scale=False, auto_bring_to_front=False)
    scatter_2.set_center_x(image_x_2 + 18)
    scatter_2.set_center_y(image_y_2 + 23)
    scatter_2.add_widget(image_2)

    image_3 = Image(source=asym_per[trial], id='img3', size=(100, 100))
    scatter_3 = Scatter(do_rotation=False, do_scale=False, auto_bring_to_front=False)
    scatter_3.set_center_x(image_x_3 + 18)
    scatter_3.set_center_y(image_y_3 + 23)
    scatter_3.add_widget(image_3)

    image_4 = Image(source=sym_ort[trial], id='img4', size=(100, 100))
    scatter_4 = Scatter(do_rotation=False, do_scale=False, auto_bring_to_front=False)
    scatter_4.set_center_x(image_x_4 + 18)
    scatter_4.set_center_y(image_y_4 + 23)
    scatter_4.add_widget(image_4)

    image_5 = Image(source=asym_ort[trial], id='img5', size=(100, 100))
    scatter_5 = Scatter(do_rotation=False, do_scale=False, auto_bring_to_front=False)
    scatter_5.set_center_x(image_x_5 + 18)
    scatter_5.set_center_y(image_y_5 + 23)
    scatter_5.add_widget(image_5)

    image_6 = Image(source=sym_per[trial], id='img6', size=(100, 100))
    scatter_6 = Scatter(do_rotation=False, do_scale=False, auto_bring_to_front=False)
    scatter_6.set_center_x(image_x_6 + 18)
    scatter_6.set_center_y(image_y_6 + 23)
    scatter_6.add_widget(image_6)

    image_7 = Image(source=asym_per[trial], id='img7', size=(100, 100))
    scatter_7 = Scatter(do_rotation=False, do_scale=False, auto_bring_to_front=False)
    scatter_7.set_center_x(image_x_7 + 18)
    scatter_7.set_center_y(image_y_7 + 23)
    scatter_7.add_widget(image_7)

    def __init__(self, *args, **kwargs):
        super(Experiment, self).__init__(*args, **kwargs)
        self.scatter_0.size_hint = [0.08, 0.09]
        self.scatter_1.size_hint = [0.08, 0.09]
        self.scatter_2.size_hint = [0.08, 0.09]
        self.scatter_3.size_hint = [0.08, 0.09]
        self.scatter_4.size_hint = [0.08, 0.09]
        self.scatter_5.size_hint = [0.08, 0.09]
        self.scatter_6.size_hint = [0.08, 0.09]
        self.scatter_7.size_hint = [0.08, 0.09]

        self.file = pd.DataFrame()

        self.submit = Button(text='Submit!', font_size=18, size_hint=(0.1, 0.1), pos=(715, 5))
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        self.add_widget(self.scatter_0)
        self.add_widget(self.scatter_1)
        self.add_widget(self.scatter_2)
        self.add_widget(self.scatter_3)
        self.add_widget(self.scatter_4)
        self.add_widget(self.scatter_5)
        self.add_widget(self.scatter_6)
        self.add_widget(self.scatter_7)

        with self.canvas:
            Line(width=5, circle=(475, 300, 275))

    def pressed(self, instance):
        if self.trial == 0:
            self.file.loc[self.trial, 'X'] = self.scatter_0.x
            self.file.loc[self.trial, 'Y'] = self.scatter_0.y
            self.file.loc[self.trial + 1, 'X'] = self.scatter_1.x
            self.file.loc[self.trial + 1, 'Y'] = self.scatter_1.y
            self.file.loc[self.trial + 2, 'X'] = self.scatter_2.x
            self.file.loc[self.trial + 2, 'Y'] = self.scatter_2.y
            self.file.loc[self.trial + 3, 'X'] = self.scatter_3.x
            self.file.loc[self.trial + 3, 'Y'] = self.scatter_3.y
            self.file.loc[self.trial + 4, 'X'] = self.scatter_4.x
            self.file.loc[self.trial + 4, 'Y'] = self.scatter_4.y
            self.file.loc[self.trial + 5, 'X'] = self.scatter_5.x
            self.file.loc[self.trial + 5, 'Y'] = self.scatter_5.y
            self.file.loc[self.trial + 6, 'X'] = self.scatter_6.x
            self.file.loc[self.trial + 6, 'Y'] = self.scatter_6.y
            self.file.loc[self.trial + 7, 'X'] = self.scatter_7.x
            self.file.loc[self.trial + 7, 'Y'] = self.scatter_7.y

            self.file.loc[self.trial, 'Image type'] = self.image_0.source
            self.file.loc[self.trial + 1, 'Image type'] = self.image_1.source
            self.file.loc[self.trial + 2, 'Image type'] = self.image_2.source
            self.file.loc[self.trial + 3, 'Image type'] = self.image_3.source
            self.file.loc[self.trial + 4, 'Image type'] = self.image_4.source
            self.file.loc[self.trial + 5, 'Image type'] = self.image_5.source
            self.file.loc[self.trial + 6, 'Image type'] = self.image_6.source
            self.file.loc[self.trial + 7, 'Image type'] = self.image_7.source

            self.image_0.source = self.sym_ort[self.trial + 1]
            self.scatter_0.set_center_x(self.image_x_0)
            self.scatter_0.set_center_y(self.image_y_0)

            self.image_1.source = self.asym_ort[self.trial + 1]
            self.scatter_1.set_center_x(self.image_x_1)
            self.scatter_1.set_center_y(self.image_y_1)

            self.image_2.source = self.sym_per[self.trial + 1]
            self.scatter_2.set_center_x(self.image_x_2)
            self.scatter_2.set_center_y(self.image_y_2)

            self.image_3.source = self.asym_per[self.trial + 1]
            self.scatter_3.set_center_x(self.image_x_3)
            self.scatter_3.set_center_y(self.image_y_3)

            self.image_4.source = self.sym_ort[self.trial + 1]
            self.scatter_4.set_center_x(self.image_x_4)
            self.scatter_4.set_center_y(self.image_y_4)

            self.image_5.source = self.asym_ort[self.trial + 1]
            self.scatter_5.set_center_x(self.image_x_5)
            self.scatter_5.set_center_y(self.image_y_5)

            self.image_6.source = self.sym_per[self.trial + 1]
            self.scatter_6.set_center_x(self.image_x_6)
            self.scatter_6.set_center_y(self.image_y_6)

            self.image_7.source = self.asym_per[self.trial + 1]
            self.scatter_7.set_center_x(self.image_x_7)
            self.scatter_7.set_center_y(self.image_y_7)
        elif self.trial == 1:
            self.file.loc[self.trial + 7, 'X'] = self.scatter_0.x
            self.file.loc[self.trial + 7, 'Y'] = self.scatter_0.y
            self.file.loc[self.trial + 8, 'X'] = self.scatter_1.x
            self.file.loc[self.trial + 8, 'Y'] = self.scatter_1.y
            self.file.loc[self.trial + 9, 'X'] = self.scatter_2.x
            self.file.loc[self.trial + 9, 'Y'] = self.scatter_2.y
            self.file.loc[self.trial + 10, 'X'] = self.scatter_3.x
            self.file.loc[self.trial + 10, 'Y'] = self.scatter_3.y
            self.file.loc[self.trial + 11, 'X'] = self.scatter_4.x
            self.file.loc[self.trial + 11, 'Y'] = self.scatter_4.y
            self.file.loc[self.trial + 12, 'X'] = self.scatter_5.x
            self.file.loc[self.trial + 12, 'Y'] = self.scatter_5.y
            self.file.loc[self.trial + 13, 'X'] = self.scatter_6.x
            self.file.loc[self.trial + 13, 'Y'] = self.scatter_6.y
            self.file.loc[self.trial + 14, 'X'] = self.scatter_7.x
            self.file.loc[self.trial + 14, 'Y'] = self.scatter_7.y

            self.file.loc[self.trial + 7, 'Image type'] = self.image_0.source
            self.file.loc[self.trial + 8, 'Image type'] = self.image_1.source
            self.file.loc[self.trial + 9, 'Image type'] = self.image_2.source
            self.file.loc[self.trial + 10, 'Image type'] = self.image_3.source
            self.file.loc[self.trial + 11, 'Image type'] = self.image_4.source
            self.file.loc[self.trial + 12, 'Image type'] = self.image_5.source
            self.file.loc[self.trial + 13, 'Image type'] = self.image_6.source
            self.file.loc[self.trial + 14, 'Image type'] = self.image_7.source

            self.file.to_excel('x_and_y.xlsx')

            self.image_0.source = self.sym_ort[self.trial + 1]
            self.scatter_0.set_center_x(self.image_x_0)
            self.scatter_0.set_center_y(self.image_y_0)

            self.image_1.source = self.asym_ort[self.trial + 1]
            self.scatter_1.set_center_x(self.image_x_1)
            self.scatter_1.set_center_y(self.image_y_1)

            self.image_2.source = self.sym_per[self.trial + 1]
            self.scatter_2.set_center_x(self.image_x_2)
            self.scatter_2.set_center_y(self.image_y_2)

            self.image_3.source = self.asym_per[self.trial + 1]
            self.scatter_3.set_center_x(self.image_x_3)
            self.scatter_3.set_center_y(self.image_y_3)

            self.image_4.source = self.sym_ort[self.trial + 1]
            self.scatter_4.set_center_x(self.image_x_4)
            self.scatter_4.set_center_y(self.image_y_4)

            self.image_5.source = self.asym_ort[self.trial + 1]
            self.scatter_5.set_center_x(self.image_x_5)
            self.scatter_5.set_center_y(self.image_y_5)

            self.image_6.source = self.sym_per[self.trial + 1]
            self.scatter_6.set_center_x(self.image_x_6)
            self.scatter_6.set_center_y(self.image_y_6)

            self.image_7.source = self.asym_per[self.trial + 1]
            self.scatter_7.set_center_x(self.image_x_7)
            self.scatter_7.set_center_y(self.image_y_7)
        elif self.trial == 2:
            self.file.loc[self.trial + 14, 'X'] = self.scatter_0.x
            self.file.loc[self.trial + 14, 'Y'] = self.scatter_0.y
            self.file.loc[self.trial + 15, 'X'] = self.scatter_1.x
            self.file.loc[self.trial + 15, 'Y'] = self.scatter_1.y
            self.file.loc[self.trial + 16, 'X'] = self.scatter_2.x
            self.file.loc[self.trial + 16, 'Y'] = self.scatter_2.y
            self.file.loc[self.trial + 17, 'X'] = self.scatter_3.x
            self.file.loc[self.trial + 17, 'Y'] = self.scatter_3.y
            self.file.loc[self.trial + 18, 'X'] = self.scatter_4.x
            self.file.loc[self.trial + 18, 'Y'] = self.scatter_4.y
            self.file.loc[self.trial + 19, 'X'] = self.scatter_5.x
            self.file.loc[self.trial + 19, 'Y'] = self.scatter_5.y
            self.file.loc[self.trial + 20, 'X'] = self.scatter_6.x
            self.file.loc[self.trial + 20, 'Y'] = self.scatter_6.y
            self.file.loc[self.trial + 21, 'X'] = self.scatter_7.x
            self.file.loc[self.trial + 21, 'Y'] = self.scatter_7.y

            self.file.loc[self.trial + 14, 'Image type'] = self.image_0.source
            self.file.loc[self.trial + 15, 'Image type'] = self.image_1.source
            self.file.loc[self.trial + 16, 'Image type'] = self.image_2.source
            self.file.loc[self.trial + 17, 'Image type'] = self.image_3.source
            self.file.loc[self.trial + 18, 'Image type'] = self.image_4.source
            self.file.loc[self.trial + 19, 'Image type'] = self.image_5.source
            self.file.loc[self.trial + 20, 'Image type'] = self.image_6.source
            self.file.loc[self.trial + 21, 'Image type'] = self.image_7.source

            self.image_0.source = self.sym_ort[self.trial + 1]
            self.scatter_0.set_center_x(self.image_x_0)
            self.scatter_0.set_center_y(self.image_y_0)

            self.image_1.source = self.asym_ort[self.trial + 1]
            self.scatter_1.set_center_x(self.image_x_1)
            self.scatter_1.set_center_y(self.image_y_1)

            self.image_2.source = self.sym_per[self.trial + 1]
            self.scatter_2.set_center_x(self.image_x_2)
            self.scatter_2.set_center_y(self.image_y_2)

            self.image_3.source = self.asym_per[self.trial + 1]
            self.scatter_3.set_center_x(self.image_x_3)
            self.scatter_3.set_center_y(self.image_y_3)

            self.image_4.source = self.sym_ort[self.trial + 1]
            self.scatter_4.set_center_x(self.image_x_4)
            self.scatter_4.set_center_y(self.image_y_4)

            self.image_5.source = self.asym_ort[self.trial + 1]
            self.scatter_5.set_center_x(self.image_x_5)
            self.scatter_5.set_center_y(self.image_y_5)

            self.image_6.source = self.sym_per[self.trial + 1]
            self.scatter_6.set_center_x(self.image_x_6)
            self.scatter_6.set_center_y(self.image_y_6)

            self.image_7.source = self.asym_per[self.trial + 1]
            self.scatter_7.set_center_x(self.image_x_7)
            self.scatter_7.set_center_y(self.image_y_7)
        elif self.trial == 3:
            self.file.loc[self.trial + 21, 'X'] = self.scatter_0.x
            self.file.loc[self.trial + 21, 'Y'] = self.scatter_0.y
            self.file.loc[self.trial + 22, 'X'] = self.scatter_1.x
            self.file.loc[self.trial + 22, 'Y'] = self.scatter_1.y
            self.file.loc[self.trial + 23, 'X'] = self.scatter_2.x
            self.file.loc[self.trial + 23, 'Y'] = self.scatter_2.y
            self.file.loc[self.trial + 24, 'X'] = self.scatter_3.x
            self.file.loc[self.trial + 24, 'Y'] = self.scatter_3.y
            self.file.loc[self.trial + 25, 'X'] = self.scatter_4.x
            self.file.loc[self.trial + 25, 'Y'] = self.scatter_4.y
            self.file.loc[self.trial + 26, 'X'] = self.scatter_5.x
            self.file.loc[self.trial + 26, 'Y'] = self.scatter_5.y
            self.file.loc[self.trial + 27, 'X'] = self.scatter_6.x
            self.file.loc[self.trial + 27, 'Y'] = self.scatter_6.y
            self.file.loc[self.trial + 28, 'X'] = self.scatter_7.x
            self.file.loc[self.trial + 28, 'Y'] = self.scatter_7.y

            self.file.loc[self.trial + 21, 'Image type'] = self.image_0.source
            self.file.loc[self.trial + 22, 'Image type'] = self.image_1.source
            self.file.loc[self.trial + 23, 'Image type'] = self.image_2.source
            self.file.loc[self.trial + 24, 'Image type'] = self.image_3.source
            self.file.loc[self.trial + 25, 'Image type'] = self.image_4.source
            self.file.loc[self.trial + 26, 'Image type'] = self.image_5.source
            self.file.loc[self.trial + 27, 'Image type'] = self.image_6.source
            self.file.loc[self.trial + 28, 'Image type'] = self.image_7.source

            self.image_0.source = self.sym_ort[self.trial + 1]
            self.scatter_0.set_center_x(self.image_x_0)
            self.scatter_0.set_center_y(self.image_y_0)

            self.image_1.source = self.asym_ort[self.trial + 1]
            self.scatter_1.set_center_x(self.image_x_1)
            self.scatter_1.set_center_y(self.image_y_1)

            self.image_2.source = self.sym_per[self.trial + 1]
            self.scatter_2.set_center_x(self.image_x_2)
            self.scatter_2.set_center_y(self.image_y_2)

            self.image_3.source = self.asym_per[self.trial + 1]
            self.scatter_3.set_center_x(self.image_x_3)
            self.scatter_3.set_center_y(self.image_y_3)

            self.image_4.source = self.sym_ort[self.trial + 1]
            self.scatter_4.set_center_x(self.image_x_4)
            self.scatter_4.set_center_y(self.image_y_4)

            self.image_5.source = self.asym_ort[self.trial + 1]
            self.scatter_5.set_center_x(self.image_x_5)
            self.scatter_5.set_center_y(self.image_y_5)

            self.image_6.source = self.sym_per[self.trial + 1]
            self.scatter_6.set_center_x(self.image_x_6)
            self.scatter_6.set_center_y(self.image_y_6)

            self.image_7.source = self.asym_per[self.trial + 1]
            self.scatter_7.set_center_x(self.image_x_7)
            self.scatter_7.set_center_y(self.image_y_7)

            self.scatter_0.remove_widget(self.image_0)
            self.scatter_1.remove_widget(self.image_1)
            self.scatter_2.remove_widget(self.image_2)
            self.scatter_3.remove_widget(self.image_3)
            self.scatter_4.remove_widget(self.image_4)
            self.scatter_5.remove_widget(self.image_5)
            self.scatter_6.remove_widget(self.image_6)
            self.scatter_7.remove_widget(self.image_7)

            self.file.to_excel('x_and_y.xlsx')

            self.submit.text = 'End of EXP!'
            self.submit.font_size = 12

        self.trial += 1



class MyEXP(App):
    def build(self):
        move = Experiment()
        return move

if __name__ == '__main__':
    MyEXP().run()
