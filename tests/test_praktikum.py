import runpy


def test_praktikum_main_prints_expected_receipt(capsys):
    runpy.run_module("praktikum.praktikum", run_name="__main__")

    assert capsys.readouterr().out == "\n".join(
        [
            "(==== black bun ====)",
            "= sauce sour cream =",
            "= filling cutlet =",
            "= filling dinosaur =",
            "(==== black bun ====)",
            "",
            "Price: 700",
            "",
        ]
    )
