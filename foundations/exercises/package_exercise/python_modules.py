# from python_basics import testing,testingMod
# import python_basics
# import sys
import sqlite3
from pathlib import Path
# from time import ctime
# import shutil
# from zipfile import ZipFile
 
# import csv
import json


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

#CSV file

#Writing CSV
# with open("data.csv","w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transcational_id","product_id","price"])
#     writer.writerow([1000,100,5000])
#     writer.writerow([2000,96,3400])

# with open("data.csv") as file:
#     reader = csv.reader(file)
#     # print(reader)
#     for readFile in reader:
#         print(readFile)

#json
# products = [
#     {
#     "userId": 1,
#     "id": 1,
#     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#     "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
#   },
#   {
#     "userId": 1,
#     "id": 2,
#     "title": "qui est esse",
#     "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
#   },
#   {
#     "userId": 1,
#     "id": 3,
#     "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
#     "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
#   },
#   {
#     "userId": 1,
#     "id": 4,
#     "title": "eum et est occaecati",
#     "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
#   }
# ]

# data = json.dumps(products)
# print(data)
# Path("products.json").write_text(data)

# Reading the JSON Data
# dataR = Path("products.json").read_text()
# productsR = json.loads(dataR)
# print(productsR)

#timestamp
# import time
# from datetime import datetime

# print (time.time())
# print(time.perf_counter())

# start = time.time()
# start = time.perf_counter()
# for i in range(1000):
  # pass

# end = time.time()
# end = time.perf_counter()
# duration = end-start
# print(duration)

# dt1 = datetime(2022,4,12)
# dt2 = datetime.now()
# dt = datetime.strptime("2033/03/22","%Y/%m/%d")
# dt = datetime.fromtimestamp(time.time())
# print(dt.day)
# print(dt.strftime("%Y"))
# print(dt2 > dt1)

#sqlite
#readJson
# jsonProducts = json.loads(Path("/Users/syedzuberiashabnam/Desktop/AI-Engineering-journal/foundations/exercises/package_exercise/products.json").read_text())
# print(jsonProducts)

#storing in database
# with  sqlite3.connect("db.sqlite3") as con:
#   command = "INSERT INTO Products VALUES(?,?,?,?,?)"
#   for product in jsonProducts:
#     con.execute(command,tuple(product.values()))
#     con.commit()

#reading from database
# with sqlite3.connect("db.sqlite3") as con:
#       command = "SELECT * FROM PRODUCTS"
#       cursor = con.execute(command)
#       products = cursor.fetchall()
#       print(products)