import click

from domain_counter.engine import make_result


@click.command()
@click.help_option("-h", "--help")
@click.version_option(
    "0.1.0", "-v", "--version", help="output the version number"
)
@click.argument("file_path", metavar="<file_path>")
def arg_parse(file_path: str) -> None:
    make_result(file_path)
