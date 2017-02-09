import os
import json
import requests
from argparse import ArgumentParser
import shutil
from pprint import pprint


USERNAME = ""
PASSWORD = ""
API_ORGS = 'https://git.generalassemb.ly/api/v3/orgs/'
ORGS = ['dsi-projects',
        'dsi-lessons',
        'dsi-labs',
        'dsi-exercises',
        'dsi-standard-curriculum',
        'dsi-playground',
        'dsi-resources']


if __name__ == "__main__":

    parser = ArgumentParser(description='Clone or pull repos from GA github enterprise in batch.')
    parser.add_argument('-d','--destination',
                        default=os.getcwd(), type=str, nargs=1,
                        help='Destination directory for repos (defaults to current).')
    parser.add_argument('-u','--username', default=None,
                        type=str, nargs=1,
                        help='Username for GA github enterprise. If not provided you must hardcorde this in the script.')
    parser.add_argument('-p','--password', default=None,
                        type=str, nargs=1,
                        help='Username for GA github enterprise. If not provided you must hardcorde this in the script.')
    parser.add_argument('-f','--overwrite','--force', default=False,
                        action='store_true',
                        help='If cloning, the folder will be deleted and re-cloned.')

    args = parser.parse_args()
    if args.username is not None:
        USERNAME = args.username[0]
    if args.password is not None:
        PASSWORD = args.password[0]
    OVERWRITE = args.overwrite
    DESTINATION = args.destination

    for org in ORGS:
        org_dir = os.path.join(DESTINATION, org)
        if os.path.exists(org_dir):
            if not OVERWRITE:
                print "directory", org, 'exists.'
            else:
                print 'removing directory', org
                shutil.rmtree(org_dir)

        if not os.path.exists(org_dir):
            os.makedirs(org_dir)
            os.chdir(org_dir)

            print "Connecting to github"
            try:
                r = requests.get(os.path.join(API_ORGS, org, 'repos?per_page=1000'), auth=(USERNAME, PASSWORD), verify=True)
                json = r.json()

                for repo in json:
                    print 'cloning repo:', repo['clone_url']
                    try:
                        os.system('git clone ' + repo['clone_url'])
                    except:
                        print 'failed to clone', repo['clone_url']
            except:
                print 'failed to connect to', org, 'repos...'

        os.chdir(DESTINATION)
