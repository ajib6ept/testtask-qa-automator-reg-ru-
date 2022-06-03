from click.testing import CliRunner

from domain_counter.cli import arg_parse
from domain_counter.engine import make_result

INPUT_DOMAIN_PATH = "tests/fixtures/domain_input.txt"
CORRECT_OUTPUT = (
    "\n".join(
        [
            "mail.ru\t2",
            "vk.com\t1",
            "rambler.ru\t1",
            "localhost\t1",
            "иванов.рф\t1",
            "xn--c1ad6a.xn--p1ai\t1",
            "INVALID\t1",
        ]
    )
    + "\n"
)


def test_func(capfd):
    make_result(INPUT_DOMAIN_PATH)
    out, err = capfd.readouterr()
    assert out == CORRECT_OUTPUT


def test_programm():
    runner = CliRunner()
    result = runner.invoke(arg_parse, [INPUT_DOMAIN_PATH])
    assert result.exit_code == 0
    assert result.output == CORRECT_OUTPUT


def test_bad_file_path():
    runner = CliRunner()
    result = runner.invoke(arg_parse, ["123111.txt"])
    assert result.exit_code == 1


def test_empty_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("empty_file.txt", "w") as f:
            f.write("")

        result = runner.invoke(arg_parse, ["empty_file.txt"])
        assert result.exit_code == 0
        assert result.output == ""
