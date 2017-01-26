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
OVERWRITE = True


if __name__ == "__main__":

    curdir = os.getcwd()

    for org in ORGS:
        org_dir = os.path.join(curdir, org)
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

        os.chdir(curdir)
