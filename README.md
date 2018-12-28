# RenameBox
simple tool for renaming filesname

# Installing Packages
1. Clone the repository to your local system using ```git clone``` or extract the downloaded zip file.
2. Run **requirements.txt** on command prompt/shell using pip.

```
  pip install -r requirements.txt
```
3. If error related to image or ImageTk still persists, run the following commands:

```
  pip install image
````

For Linux systems, run the given command on shell:
```
  sudo apt-get install python3-pil.imagetk
```

### How to use 
```
 $ python3 renameBox.py
 ```
 Then input the directory where images are stored. 
 It will automatically create new directory (OldDirectory to OldDirectory_new) where renamed file will be stored.
