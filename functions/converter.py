import os 
from subprocess import call
from autocorrect import Speller

spell = Speller(lang='en')

def generate_summary_file(book_parent_foulder):
    
    print("book foulder:", book_parent_foulder)
    scr_foulder = str(book_parent_foulder) + "/src"
    summary_file_name = "SUMMARY.md"


    summary_file_path = os.path.join(scr_foulder, summary_file_name)

    try:
        os.remove(summary_file_path)
        print("removed old summary file ")
    except:
        print("no summary file found ")

    all_files_and_foulders = os.walk(scr_foulder)
    foulder_rename = []
    
    all_md_files = []
    
    for (root, dirs, files) in all_files_and_foulders:
        # print("root",root)
        # print("files", files)
        new_root = os.path.join( os.path.dirname(root), root.split("/")[-1].lower().replace(" ", "-"))
        
        for file in files:
            
            if ".md" in file:
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r+') as f:
                    file_data = f.read()  
                    new_file = ""
                    if '!' in file_data:
                        for line in file_data.splitlines():
                            if '!' in line:
                                object_path = line.replace("![](", "").replace(")", "").split("/")[-1]
                                new_foulder = os.path.dirname(line.replace("![](", "").replace(")", "")).lower()
                                
                                new_line = "![](" + os.path.join(new_foulder, object_path) + ")"
                                
                                new_file = new_file + (new_line + "\n")
                            else:
                                new_file = new_file + (line + "\n")
                        print(new_file)
                        f.write(new_file)

            if not "README.md" in file:
                full_file_path = os.path.join(root, file)
                new_file_name = file.lower().replace(" ", "-")  
                new_file_name_with_path = os.path.join(root,new_file_name)
                os.rename(full_file_path, new_file_name_with_path)
        
        foulder_rename.append([root, new_root])
        print("---")
    
    foulder_rename.sort(reverse=True)
    for foulder in foulder_rename:
        os.rename(foulder[0], foulder[1])


    cmd = f'mdbook-auto-gen-summary gen -t {scr_foulder}'
    call(cmd, shell=True)


    new_file = ""
    with open(summary_file_path, 'r') as f:
        for line in f:
            if "[" in line and "-" in line:
                braket_text = "[" + line.split("]")[0].split("[")[-1] + "]"
                new_braket_text = spell(braket_text.replace("-", " "))
                
                new_line = line.replace(braket_text, new_braket_text)
                new_file = new_file + new_line


            
            else:
                new_file = new_file + line

    # print(new_file)
    try:
        os.remove(summary_file_path)
        print("removed old summary file ")
    except:
        print("no summary file found ")



    with open(summary_file_path, 'w') as f:
        f.write(new_file)
