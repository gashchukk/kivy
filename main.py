from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        label = Label(text='Це перший екран', size_hint=(1, 0.1))
        button = Button(text='Перейти до другого екрану', size_hint=(1, 0.1))
        button.bind(on_press=self.go_to_second_screen)

        self.text_input = TextInput(hint_text='Введіть ваше ім\'я', size_hint=(1, 0.1))

        layout.add_widget(label)
        layout.add_widget(self.text_input)
        layout.add_widget(button)
        self.add_widget(layout)

    def go_to_second_screen(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        label = Label(text='Це другий екран', size_hint=(1, 0.1))
        button = Button(text='Повернутися до першого екрану', size_hint=(1, 0.1))
        button.bind(on_press=self.go_to_first_screen)

        self.slider = Slider(min=0, max=100, value=50, size_hint=(1, 0.1))
        self.slider_label = Label(text=f'Значення: {self.slider.value}', size_hint=(1, 0.1))
        self.slider.bind(value=self.on_slider_value_change)

        layout.add_widget(label)
        layout.add_widget(self.slider_label)
        layout.add_widget(self.slider)
        layout.add_widget(button)
        self.add_widget(layout)

    def on_slider_value_change(self, instance, value):
        self.slider_label.text = f'Значення: {value}'

    def go_to_first_screen(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'


class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        return sm


if __name__ == '__main__':
    MyApp().run()
