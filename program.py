'''Класс которы йотвечает за сравнивание следующих цветов: красный(К), зеленый(З) и синий(С)'''
class CompareColors():
    def __init__(self):
        self.filtered_colors = []

    '''Метод ввода данных цветов и преобразования их в верхний регистр'''
    def input_colors(self):
        input_colors = (input("Через пробел введите объекты красного, зеленого и синего цвета, используя следующие сокращения К (для красного цвета), З (для зеленого цвета) и С (для синего цвета): ")).upper()
        return input_colors

    '''Метод очистки введеного списка цветов от лишних символов'''
    def clear_the_list_of_unnecessary_characters(self, input_colors):
        self.input_colors = input_colors
        symbols_to_remove = ", /.!&+-;"

        # Удаление из строки введенных цветов лишних символов
        for symbol in symbols_to_remove:
            input_colors = input_colors.replace(symbol, "")
        return input_colors

    '''Метод удаления цветов не относящихся к З, С и К'''
    def make_colors_list_without_other_characters(self, value):
        self.value = value
        list_true = ['З', 'С', 'К']

        # Добавление в список цветов входящих в список разрешенных
        for n in value:
            if n in list_true:
                self.filtered_colors.append(n)
        return self.filtered_colors

    '''Метод ввода правила для сравнения цветов'''
    def input_rule_for_compare_colors(self):
        input_rule = input("Введите правило для сравнения цветов(З, С, К), используя следующие знаки: >, ==, < \nПример: З < C < К \n")
        return input_rule

    '''Метод сортировки цветов в зависимости от правила сортировки'''
    def sort_colors_by_rule(self, input_rule):
        # Удаление пробелов
        normalized_rule = input_rule.replace(" ", "")

        # Проверка на равные приоритеты
        if "==" in normalized_rule:
            return self.filtered_colors.copy()

        # Определение направления сортировки
        if ">" in normalized_rule:
            reverse = True
        elif "<" in normalized_rule:
            reverse = False
        else:
            print("Неизвестное правило сортировки")
            return None

        # Извлечение уникальных цветов из правила в порядке следования
        colors_in_rule = []
        for char in normalized_rule:
            if char in {'З', 'С', 'К'} and char not in colors_in_rule:
                colors_in_rule.append(char)

        # Если в правиле меньше 2 цветов, сортировка невозможна
        if len(colors_in_rule) < 2:
            print("Недостаточно цветов в правиле для сортировки")
            return None

        # Создание порядка сортировки на основе правила
        color_order = {color: idx for idx, color in enumerate(colors_in_rule)}

        # Сортировка с учетом направления
        return sorted(
            self.filtered_colors,
            key=lambda x: color_order.get(x, len(color_order)),
            reverse=reverse
        )


color_processor = CompareColors()
raw_input = color_processor.input_colors()
cleaned_input = color_processor.clear_the_list_of_unnecessary_characters(raw_input)
filtered_colors = color_processor.make_colors_list_without_other_characters(cleaned_input)
rule = color_processor.input_rule_for_compare_colors()
sort_list = color_processor.sort_colors_by_rule(rule)
print(f"Результат сортировки: {sort_list}")