from user_input import get_data
import rational_calc as calc
import view
import complex_calc


def controller():
    user_choice = view.main_choice_window()

    if user_choice == 'Калькулятор':
        user_input = get_data('Калькулятор', 'Введите выражение:')
        result = calc.rational_calc_func(user_input)
        if view.result_window('Результат', str(result)):
            return controller()
        else:
            return view.exit_window()
    if user_choice == 'Калькулятор комплексных чисел':
        user_input = get_data('Калькулятор комплексных чисел', 'Введите выражение:')
        result = complex_calc.complex_calc_func(user_input)
        if view.result_window('Результат', str(result)):
            return controller()
        else:
            return view.exit_window()
    if user_choice == 'Журнал логов':
        view.log_window()
        return controller()
    else:
        return view.exit_window()
