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
import time, asyncio, pprint, random


async def worker(name, queue):
    while True:
        test = await queue.get()
        pprint.pprint(f'{test:.2f}')
        await asyncio.sleep(test)
        queue.task_done()
        print(f'{name} has slept for {test:.2f} seconds')


def version():
    print("vor-mon.py -- 0.0.1")
    return 0


async def main(options):
    # TODO: Do something more interesting here...
    queue = asyncio.Queue()
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.gauss(1, .5)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)
    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')
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
            #funcReturn = main(options)
            funcReturn = asyncio.run(main(options))
        if options.version == True:
            funcReturn = version()
        if options.verbose:
            print(time.asctime())
        if options.verbose:
            print("TOTAL TIME IN SECONDS:")
        if options.verbose:
            print((time.time() - start_time))
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
