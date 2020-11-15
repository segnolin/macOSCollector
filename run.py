import argparse
import datetime
import glob
import importlib
import json
import os
import sys

def exectue(command):
    print(f'[*] Executing: {command}')
    return os.system(command)

def install():
    with open('./requirements.json') as json_file:
        data = json.load(json_file)
        if not os.path.exists('./submodules'):
            os.makedirs('./submodules')
        for requirement in data:
            name = requirement['name']
            print(f'[*] Installing Submodule: {name}')
            for command in requirement['commands']:
                result = exectue(command)
                if result:
                    print('[*] Error')
                    break

def collect():
    with open('./submodules.json') as json_file:
        data = json.load(json_file)
        if not os.path.exists('./artifacts'):
            os.makedirs('./artifacts')
        for submodule in data:
            name = submodule['name']
            print(f'[*] Running Submodule: {name}')
            if not os.path.exists(f'./artifacts/{name}'):
                os.makedirs(f'./artifacts/{name}')
            for command in submodule['commands']:
                result = exectue(command)
                if result:
                    print('[*] Error')
                    break
            module = importlib.import_module(f'modules.{name}')
            module.parse()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--install',
            help='installing requirements for submodules',
            action='store_true')
    parser.add_argument('-c', '--collect',
            help='collecting artifacts',
            action='store_true')
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.error('no arguments provided')

    if args.install:
        install()
    if args.collect:
        collect()

if __name__ == '__main__':
    main()
