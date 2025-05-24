# -*- coding: utf-8 -*-
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys

from chibi.config import basic_config, load as load_config
from chibi.config import default_file_load, configuration


default_file_load( '{{cookiecutter.project_slug}}.py', touch=False )

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
parser = argparse.ArgumentParser(
    description="{{cookiecutter.project_short_description}}", fromfile_prefix_chars='@'
)

parser.add_argument(
    "params", nargs='+', metavar="params",
    help="argumentos de cli" )

parser.add_argument(
    "--log_level", dest="log_level", default="INFO",
    help="nivel de log",


def main():
    """Console script for {{cookiecutter.project_slug}}."""
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    basic_config( args.log_level )

    for i, a in args.params:
        print( f"argumento {i}: {a}" )

    print( "Cambia este mensaje en{{cookiecutter.project_slug}}.cli.main" )
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
