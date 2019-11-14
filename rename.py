import os
from os import remove, close
from os import rename
from os.path import join, isfile
from shutil import move
from subprocess import call
from tempfile import mkstemp


def replace_djang_base(path, project_name):
    for dirname in os.listdir(path):
        try:
            if dirname not in [".sass-cache", "bower_components", "node_modules", ".git", "db.sqlite3", "migrations"]:
                if isfile(join(path, dirname)):
                    replace(join(path, dirname), "hr_system", project_name)
                else:
                    replace_djang_base(join(path, dirname), project_name)
        except:
            pass


def replace(file_path, pattern, subst):
    # Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


project_name = input("Enter project name (default:nameless): ") or "nameless"
project_path = os.path.dirname(os.path.abspath(__file__))
# rename(join(project_path, "docker-build"), join(project_path, project_name + "-docker-build"))
rename(join(project_path, "hr_system"), join(project_path, project_name))
replace_djang_base(project_path, project_name)
call(["rm", os.path.abspath(__file__)])
