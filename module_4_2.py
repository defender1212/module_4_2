def test_function():
    def inner_function():
        a = 5
        print('Я в области видимости функции test_function')
    inner_function()
test_function()
