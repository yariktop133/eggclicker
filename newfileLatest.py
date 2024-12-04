import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout


class EggClickerApp(App):
    def build(self):
        self.egg_counts = {
            "Чёрное яйцо": 0,
            "Золотое яйцо": 0,
            "Зелёное яйцо": 0,
            "Серое яйцо": 0,
            "Белое яйцо": 0,
        }

        # Основной контейнер с фоном
        self.layout = RelativeLayout()

        # Фон
        self.layout.add_widget(Image(source="background.jpg", allow_stretch=True, keep_ratio=False))

        # Внутренний контейнер для кнопки и текста
        inner_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Кнопка с текстурой
        self.click_button = Button(
            text="Нажимай и выбивай яйца",
            size_hint=(1.1, 1.1),
            font_size=50,
            background_normal="button_normal.png",  # Текстура кнопки в нормальном состоянии
            background_down="button_down.png",  # (Опционально) Текстура кнопки при нажатии
        )
        self.click_button.bind(on_press=self.handle_click)

        # Отображение результатов
        self.result_label = Label(
            text="Нажимай и выбивай яйца!",
            font_size=80,
            halign="center",
            valign="middle",
        )
        self.result_label.bind(size=self.result_label.setter("text_size"))

        # Статистика
        self.stats_label = Label(
            text=self.get_stats(),
            font_size=60,
            halign="left",
            valign="top",
        )
        self.stats_label.bind(size=self.stats_label.setter("text_size"))

        # Добавление виджетов в контейнер
        inner_layout.add_widget(self.click_button)
        inner_layout.add_widget(self.result_label)
        inner_layout.add_widget(self.stats_label)

        # Добавляем внутренний контейнер поверх фона
        self.layout.add_widget(inner_layout)

        return self.layout

    def handle_click(self, instance):
        # Вероятности выпадения
        chance = random.randint(1, 100)
        if chance <= 1:
            egg = "Чёрное яйцо"
        elif chance <= 10:
            egg = "Золотое яйцо"
        elif chance <= 40:
            egg = "Зелёное яйцо"
        elif chance <= 90:
            egg = "Серое яйцо"
        else:
            egg = "Белое яйцо"

        # Обновляем количество
        self.egg_counts[egg] += 1

        # Обновляем текст
        self.result_label.text = f"Ты выбил: {egg}!"
        self.stats_label.text = self.get_stats()

    def get_stats(self):
        total = sum(self.egg_counts.values())
        stats = "Стата:\n"
        for egg, count in self.egg_counts.items():
            stats += f"{egg}: {count}\n"
        stats += f"Всего: {total}\n"
        return stats


if __name__ == "__main__":
    EggClickerApp().run()