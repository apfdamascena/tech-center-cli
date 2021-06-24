import click
import os

def steps():
    if(os.path.isdir('deploying')):
        os.system("rm -rf deploying")
    os.path("mkdir deploying")
    os.path("git clone https://github.com/apfdamascena/TechCenter.git ./deploying")
    os.path("git -C ./deploying/TechCenter remote add upstream https://github.com/citi-onboarding/TechCenter.git")
    os.path("git -C ./deploying/TechCenter pull upstream deploy")
    os.path("git -C ./deploying/TechCenter checkout deploy")
    os.path("git -C ./deploying/TechCenter add .")
    os.path('git -C ./deploying/TechCenter add commit -m "deploying"')
    os.path("git -C ./deploying/TechCenter push -u origin deploy")

@click.command()
def cli():
    steps()