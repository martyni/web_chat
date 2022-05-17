#!/usr/bin/python3
import glob
import re
import os

def get_current_style_sheet_number():
   css_file_name = glob.glob("downloads/style*")[0]
   match = re.match(r"downloads/style(.*).css",css_file_name)
   return int(match.groups(1)[0])

def update_css_file_number(current_style_sheet_number):
   new_style_sheet_number = current_style_sheet_number + 1
   old_file="downloads/style{n}.css".format(n=current_style_sheet_number)
   new_file="downloads/style{n}.css".format(n=new_style_sheet_number)
   os.rename(old_file, new_file)
   return "renamed {old_file} to {new_file}".format(old_file=old_file,
           new_file=new_file) 

def update_vars_file(current_style_sheet_number):
    n = current_style_sheet_number + 1
    with open("vars.py","w") as var_file:
        file_contents = 'STYLE_SHEET_NUMBER={}'.format(n)
        var_file.write(file_contents)
    return file_contents

def main():
   n = get_current_style_sheet_number()
   print(update_css_file_number(n))
   print(update_vars_file(n))

if __name__ == "__main__":
   main()
    
