import os 
from subprocess import call
import shutil
from functions.converter import generate_summary_file

command = input()
# command = "/home/lyonh/Downloads/micro_usd_pipline, trillium-Book, /home/lyonh/Documents"

path_to_trillium_export = command.split(",")[0]
book_name = command.split(",")[-2].replace(" ", "")
book_parent_path = command.split(",")[-1]
book_path = os.path.join(book_parent_path, book_name)[1:]
book_scr_path = os.path.join(book_path, "src")
trillium_important_foulder = os.path.join(path_to_trillium_export, path_to_trillium_export.split("/")[-1])



move_to_book_path = f'cd {book_parent_path}'

cmd = f'{move_to_book_path} && mdbook init {book_name} --title={book_name} --ignore=git'
call(cmd, shell=True)


shutil.rmtree(book_scr_path)
os.mkdir(book_scr_path)

shutil.copytree(trillium_important_foulder, os.path.join(book_scr_path, trillium_important_foulder.split("/")[-1]))

generate_summary_file(book_path)
