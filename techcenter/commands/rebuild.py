import click
import os

def steps():
    if(os.path.isdir('./public')):
        os.system("rm -rf ./public")
    workdir = os.getcwd()
    os.system('echo "SKIP_PREFLIGHT_CHECK=true" >> ./client/.env')
    os.system('yarn --cwd ./client build')
    while(not os.path.isdir('./client/build')):
        continue
    os.system("cp -r ./client/build ./public")
    os.system("rm -rf ./client/build")


@click.command()
def cli():
    steps()

