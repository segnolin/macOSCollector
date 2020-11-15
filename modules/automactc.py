import glob
import json
import os

def parse():
    print('[*] Parsing automactc output files')
    artifact_names = glob.glob(f'./artifacts/automactc/automactc-output*.json')
    for artifact_name in artifact_names:
        blocks = []
        if 'runtime' in artifact_name:
            os.remove(artifact_name)
            continue
        with open(artifact_name, 'r') as artifact_file:
            for line in artifact_file:
                try:
                    blocks.append(json.loads(line))
                except:
                    continue
        output = json.dumps(blocks, indent=2)
        info = artifact_name.replace('.json', '').split(',')
        os.remove(artifact_name)
        with open(f'./artifacts/automactc/{info[4]} {info[3]}.json', 'w') as artifact_file:
            artifact_file.write(output)
