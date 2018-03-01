# hashcode-2018-tabsnotspaces

Alec Doran-Twyford
Stath
Rose

## Quickstart

### PreReq

Should only need to do this if it your 1st time with Python and virtual enviroments

```bash
sudo apt-get install python-pip python-dev build-essential
sudo pip install virtualenv virtualenvwrapper
sudo pip install --upgrade pip
printf '\n%s\n%s\n%s' '# virtualenv' 'export WORKON_HOME=~/virtualenvs' \
'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
source ~/.bashrc
mkdir -p $WORKON_HOME
```

### Using Virtualenv

````bash
git clone https://github.com/hackthenight/hashcode-2018-tabsnotspaces.git
cd hashcode-2018-tabsnotspaces
virtualenv virtualenv-hashcode-2018
source virtualenv-hashcode-2018/bin/activate
pip install -r requirements.txt
````

### Using Virtualenv Wrapper

````bash
git clone https://github.com/hackthenight/hashcode-2018-tabsnotspaces.git
cd hashcode-2018-tabsnotspaces
mkvirtualenv hashcode-2018
workon hashcode-2018
pip install -r requirements.txt
````