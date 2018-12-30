# Preface
I have no idea how to use git, and it shows.

# markov-twitter
Pulls a user's tweets and runs them through a markov chain generator, then tweets the result. All this really is is a basic script.

# Installation
## Dependencies
'markov-twitter' requires [python-twitter](https://github.com/bear/python-twitter) and [markovify](https://github.com/jsvine/markovify). Install these using
'''bash
pip3 install python-twitter markovify
'''
Please note that markov-twitter is only to be used with Python 3.
## Cloning
Installation is typical. Just clone the repo into a directory of your choosing, 'cd' in, and you're ready to go.
'''bash
git clone https://github.com/hesterdakota/markov-twitter.git
cd markov-twitter
'''

# Configuration
Set up the Twitter API in 'APICredentials.py'. Further info can be found [here](https://github.com/bear/python-twitter#api).
Set the desired user target with the 'user_name' variable. Ensure that the username is a string, and do not include the @ portion of the username.
More tweaking can be found in the python-twitter docs [here](https://python-twitter.readthedocs.io/en/latest/) and the markovify docs [here](https://github.com/jsvine/markovify).

# Running
After you're set up, just run 'main.py' in Python 3. That's all.
