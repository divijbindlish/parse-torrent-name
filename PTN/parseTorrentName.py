#!/usr/bin/env python
import argparse
import PTN

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('torrent_name', help='Torrent name to parse')
    parser.add_argument('-j', '--json', dest="json", action='store_true', default=False, help='Output in json format')
    parser.add_argument('-y', '--yaml', dest="yaml", action='store_true', default=False, help='Output to YAML')
    parser.add_argument('-f', '--file', dest="filename", default=False, help='Output to file as well as command line')
    args = parser.parse_args()

    info = PTN.parse(args.torrent_name)
    if args.yaml:
        try:
            from ruamel import yaml
            output = str(yaml.dump(info, default_flow_style=False))
        except ImportError:
            print "yaml module required for yaml output!\nInstall with 'pip install ruamel.yaml'"
            exit(1)
    elif args.json:
        try:
            try:
                import simplejson as json
            except ImportError:
                import json
            output = json.dumps(info, indent=4, sort_keys=True)
        except ImportError:
            print "json module required for json output!\nInstall with 'pip install simplejson' or update python to 2.6+"
            exit(1)
    else:
        output = str(info)
    if args.filename:
        with open(args.filename, 'w') as f:
            f.write(output)
    print output
