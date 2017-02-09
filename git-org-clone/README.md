# git-org-clone.py

`git-org-clone.py` is a helper tool to automatically clone the all the repos for
an entire organization on github enterprise.

## Usage

You can use the script in a couple of ways. The first think you'll need to do is
make sure that the `API_ORGS` and `ORGS` variables are properly set. The defaults
are set up for the DSI repos:

```python
API_ORGS = 'https://git.generalassemb.ly/api/v3/orgs/'
ORGS = ['dsi-projects',
        'dsi-lessons',
        'dsi-labs',
        'dsi-exercises',
        'dsi-standard-curriculum',
        'dsi-playground',
        'dsi-resources']
```

The `API_ORGS` variable shouldn't need to change as long as you are using this
for orgs on GA's github enterprise system. `ORGS` is the list of organizations
that you want to clone. This script will clone **all** repos within each organization.

There are also `USERNAME` and `PASSWORD` variables at the top of the script.
You can enter these here or optionally enter them as arguments when calling the
script.

Command line arguments include:

```
-d, --destination : Directory where orgs will be cloned. Defaults to current.
-u, --username: Your GA github enterprise username.
-p, --password: Your GA github enterprise password.
-f, --force, --overwrite: Will delete existing orgs and re-clone them.
```

So, for example:
```
> python git-org-clone.py -u kieferk -p extremelystrongpassword -f
```

Would clone all of the repos in the orgs specified, overwriting existing
folders. Destination was not specified so it will clone orgs into their respective
folders in the current working directory.
