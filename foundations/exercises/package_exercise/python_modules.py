# from python_basics import testing,testingMod
# import python_basics
# import sys

from pathlib import Path
# from time import ctime
# import shutil
from zipfile import ZipFile
 
# python_basics.testingMod()
# testing()
# testingMod()

# print(sys.path)

# def testing():
#   pass

# def testingMod():
#   pass

# if(__name__ == '__main__'):
#   print("Practising Python")

# path = Path("/Users/syedzuberiashabnam/Desktop/AI-Engineering-journal/foundations/exercises")

# Path() / "package_exercise" / "__init__.py"

# Path.home()

# print(path.exists())
# path.is_file()
# path.is_dir()
# print(path.name,path.parent)
# path = path.with_name("file.txt")
# print(path.absolute())
# path.mkdir()
# path.rmdir()
# path.rename("python_basics")
# print(path.is_dir())
# for p in path.iterdir():
#   print(p)

# comprehension
# pathdir = [p for p in path.iterdir() if p.is_dir()]
# print(pathdir)

# py_files = [p for p in path.rglob("*.py")]

# py_files = [p for p in path.glob("**/*.py")]
# print(py_files)


# source = Path("/Users/syedzuberiashabnam/Desktop/AI-Engineering-journal/foundations/exercises/package_exercise/__init__.py")

# print(path.exists())
# print(ctime(path.stat().st_ctime))
# print(path.read_text())
# # path.write_text("...")

# target = Path() / "__init__.py"

# target.write_text(source.read_text())
# shutil.copy(source,target)

# Zip Files

# with ZipFile("packexercise.zip",'w') as zip:
#   for path in Path("/Users/syedzuberiashabnam/Desktop/AI-Engineering-journal/foundations/exercises").rglob("*.*"):
#     zip.write(path)

# with ZipFile("/Users/syedzuberiashabnam/Desktop/AI-Engineering-journal/foundations/exercises/package_exercise/packexercise.zip") as zip:
#   # print(zip.namelist())
#   info = zip.getinfo("Users/syedzuberiashabnam/Desktop/AI-Engineering-journal/foundations/exercises/python_basics.py")
#   print(info.compress_size)
#   zip.extractall("extract")
