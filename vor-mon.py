#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNOPSIS

    TODO helloworld [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    TODO This describes how to use this script. This docstring
    will be printed by the script if there is an error or
    if the user requests help (-h or --help).

EXAMPLES

    TODO: Show some examples of how to use this script.

EXIT STATUS

    TODO: List exit codes

AUTHOR

    TODO: Name <name@example.org>

LICENSE

    This script is in the public domain, free from copyrights or restrictions.
    Source material from http://code.activestate.com/recipes/528877-skeleton-script-hello-world/.

VERSION

    $Id$
"""

import sys, os, traceback, argparse
import time


def version():
    print("vor-mon.py -- 0.0.1")
    return 0


def main(options):
    # TODO: Do something more interesting here...
    print("Hello world!")
    return 0


if __name__ == "__main__":
    try:
        start_time = time.time()
        helpDescription = "TODO: Write a description"
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description=helpDescription,
        )
        parser.add_argument(
            "-v",
            "--verbose",
            action="store_true",
            default=False,
            help="Change to verbose output",
        )
        parser.add_argument(
            "--version", action="store_true", default=False, help="Print version"
        )
        options = parser.parse_args()
        if len(sys.argv) < 1:
            parser.error("missing argument")
        if options.verbose:
            print(time.asctime())
        if options.version == False:
            funcReturn = main(options)
        if options.version == True:
            funcReturn = version()
        if options.verbose:
            print(time.asctime())
        if options.verbose:
            print("TOTAL TIME IN MINUTES:")
        if options.verbose:
            print((time.time() - start_time) / 60.0)
        sys.exit(funcReturn)
    except KeyboardInterrupt as e:  # Ctrl-C
        raise e
    except SystemExit as e:  # sys.exit()
        raise e
    except Exception as e:
        print("ERROR, UNEXPECTED EXCEPTION")
        print(str(e))
        traceback.print_exc()
        os._exit(1)
