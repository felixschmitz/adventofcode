from solution import first_task, second_task


def test_first_task():
    hv_product = first_task("sample_input.txt")
    assert hv_product == 150


def test_second_task():
    hva_product = second_task("sample_input.txt")
    assert hva_product == 900
