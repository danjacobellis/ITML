def build():
    from subprocess import run
    from shutil import rmtree, copytree, copyfile
    from os.path import exists
    from pathlib import Path
    
    if exists("docs"):
        rmtree("docs")
    result = run(["sphinx-build", ".","docs"],capture_output=True)
    print(result.stdout.decode("utf-8"))
    Path("docs/.nojekyll").touch()
    
if __name__ == '__main__':
    build()