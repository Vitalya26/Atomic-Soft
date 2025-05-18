import pytest
from program import CompareColors


@pytest.fixture
def color_processor():
    return CompareColors()

'''Тест кейс 1 (см. описание в тест-кейсах)'''
def test_sort_color_objects_test_case_1(color_processor):
    input_colors = "К С З"
    cleaned = color_processor.clear_the_list_of_unnecessary_characters(input_colors)
    color_processor.make_colors_list_without_other_characters(cleaned)
    assert color_processor.sort_colors_by_rule('З < С < К') == ['З', 'С', 'К']


'''Тест кейс 2 (см. описание в тест-кейсах)'''
def test_sort_color_objects_test_case_2(color_processor):
    input_colors = "С З З З К С З"
    cleaned = color_processor.clear_the_list_of_unnecessary_characters(input_colors)
    color_processor.make_colors_list_without_other_characters(cleaned)
    assert color_processor.sort_colors_by_rule('С > З > К') == ['К', 'З', 'З', 'З', 'З', 'С', 'С']

'''Тест кейс 3 (см. описание в тест-кейсах)'''
def test_sort_color_objects_test_case_3(color_processor):
    input_colors = "С К З С К З С К З С К З"
    cleaned = color_processor.clear_the_list_of_unnecessary_characters(input_colors)
    color_processor.make_colors_list_without_other_characters(cleaned)
    assert color_processor.sort_colors_by_rule('К > З > С') == ['С', 'С', 'С', 'С', 'З', 'З', 'З', 'З', 'К', 'К', 'К', 'К']

'''Тест кейс 4 (см. описание в тест-кейсах)'''
def test_sort_color_objects_test_case_4(color_processor):
    input_colors = " С С К С С С С С К З К"
    cleaned = color_processor.clear_the_list_of_unnecessary_characters(input_colors)
    color_processor.make_colors_list_without_other_characters(cleaned)
    assert color_processor.sort_colors_by_rule('З > К > С') == ['С', 'С', 'С', 'С', 'С', 'С', 'С', 'К', 'К', 'К', 'З']

'''Тест кейс 5 (см. описание в тест-кейсах)'''
def test_sort_color_objects_test_case_5(color_processor):
    input_colors = "К З К З К З К К З З С З"
    cleaned = color_processor.clear_the_list_of_unnecessary_characters(input_colors)
    color_processor.make_colors_list_without_other_characters(cleaned)
    assert color_processor.sort_colors_by_rule('З > C > К') == ['С', 'К', 'К', 'К', 'К', 'К', 'З', 'З', 'З', 'З', 'З', 'З']

'''Тест кейс 6 (см. описание в тест-кейсах)'''
def test_sort_color_objects_test_case_6(color_processor):
    input_colors = "С С С С С С С С С К З"
    cleaned = color_processor.clear_the_list_of_unnecessary_characters(input_colors)
    color_processor.make_colors_list_without_other_characters(cleaned)
    assert color_processor.sort_colors_by_rule('З < К < С') == ['З', 'К', 'С', 'С', 'С', 'С', 'С', 'С', 'С', 'С', 'С']

'''Тест кейс 7 (см. описание в тест-кейсах)'''
def test_sort_color_objects_test_case_7(color_processor):
    input_colors = "С К З"
    cleaned = color_processor.clear_the_list_of_unnecessary_characters(input_colors)
    color_processor.make_colors_list_without_other_characters(cleaned)
    assert color_processor.sort_colors_by_rule('З == К == С') == ['С', 'К', 'З']

'''Тест кейс 8 (см. описание в тест-кейсах)'''
def test_sort_color_objects_test_case_8(color_processor):
    input_colors = "С К З С К З С К З С К З З З"
    cleaned = color_processor.clear_the_list_of_unnecessary_characters(input_colors)
    color_processor.make_colors_list_without_other_characters(cleaned)
    assert color_processor.sort_colors_by_rule('К == З == С') == ['С', 'К', 'З', 'С', 'К', 'З', 'С', 'К', 'З', 'С', 'К', 'З', 'З', 'З']
