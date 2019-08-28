#!/bin/bash
#set -x
set -e 

me=`basename "$0"`

printf "[$me] setup python virtualenv ...\n"
virtualenv --python=python3 venv 
source venv/bin/activate
which python
which pip 
python --version
pip --version 

printf "\n[$me] pip install requirements ...\n"
pip install -r requirements.txt

printf "\n[$me] git config ...\n"
git config core.hooksPath .githooks
git config -l 

printf "\n[$me] all done happy developing !!!\n"