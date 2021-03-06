# Python IDLE Package Manager  
![https://img.shields.io/badge/Python-v3.8.1-blue](https://img.shields.io/badge/Python-v3.8.1-blue)
![https://img.shields.io/github/repo-size/ZekIzLoupriora/Python-IDLE-Package-Manager?label=Repo%20Size](https://img.shields.io/github/repo-size/ZekIzLoupriora/Python-IDLE-Package-Manager?label=Repo%20Size)  
![https://img.shields.io/github/contributors-anon/ZekIzLoupriora/Python-IDLE-Package-Manager?color=green&label=Contributors](https://img.shields.io/github/contributors-anon/ZekIzLoupriora/Python-IDLE-Package-Manager?color=green&label=Contributors)
![https://img.shields.io/github/last-commit/ZekIzLoupriora/Python-IDLE-Package-Manager?color=yellow&label=Last%20Commit](https://img.shields.io/github/last-commit/ZekIzLoupriora/Python-IDLE-Package-Manager?color=yellow&label=Last%20Commit)  
![https://img.shields.io/github/issues/ZekIzLoupriora/Python-IDLE-Package-Manager?label=Issues](https://img.shields.io/github/issues/ZekIzLoupriora/Python-IDLE-Package-Manager?label=Issues)
![https://img.shields.io/github/issues-closed/ZekIzLoupriora/Python-IDLE-Package-Manager?label=Issues](https://img.shields.io/github/issues-closed/ZekIzLoupriora/Python-IDLE-Package-Manager?label=Issues)
![VulnerabilitiesShield](https://img.shields.io/snyk/vulnerabilities/github/ZekIzLoupriora/Python-IDLE-Package-Manager?label=Vulnerabilities)  
![https://img.shields.io/github/license/ZekIzLoupriora/Python-IDLE-Package-Manager?label=License&logo=License](https://img.shields.io/github/license/ZekIzLoupriora/Python-IDLE-Package-Manager?label=License&logo=License)  
A simple package manager extension with GUI for the default Python IDLE
____
## Table of contents
1. [Installation](#Installation)
2. [Screenshots](#Screenshots)
3. [FAQ](#FAQ)
____
## Installation
1. Clone this repo or download it as a ZIP archive;
2. Install dependencies:
```
pip install PyQt5 urllib3 requests lxml
```
or using **requirements.txt** file (preferred):
```
pip install -r requirements.txt
```
3. Open your Python installation directory (it is usually located at /path/to/your/user/folder/AppData/Local/Programs/Python/PythonXX-YY);
4. Put the **PipGUI.py** and **PacMan** folder into the **/Lib/idlelib/** directory; it should look something like this:  
![???????????? ???????????? 2022-04-10 125829](https://user-images.githubusercontent.com/38569354/162608531-7514bc24-77c8-4001-a961-8a33a08d9d41.png)
![???????????? ???????????? 2022-04-10 125801](https://user-images.githubusercontent.com/38569354/162608515-82859375-1a3a-4abd-9e18-f94d7485bc9b.png)
5. Locate the **editor.py** file in the **/Lib/idlelib/** directory and open it with the text editor of your choice;
6. Search for **menu_specs**; it should look something like this:
![???????????? ???????????? 2022-04-10 130146](https://user-images.githubusercontent.com/38569354/162608639-a7a993f7-937f-4144-a925-d71880512453.png)
7. Add the following line to the end of this list: **```("pacman", "Pac_Man"),```**  
Now it should look like this:  
![???????????? ???????????? 2022-04-10 130524](https://user-images.githubusercontent.com/38569354/162608794-0229287c-a5d7-474a-a5db-7a0a2d90d81b.png)
8. **Optional:** Do steps 5-7 with the **pyshell.py** file (if you don't, you will not see **PacMan** menu entry while running scripts via IDLE);
9. Locate the **config-extensions.def** file in the **/Lib/idlelib/** directory and open it with the text editor of your choice;
10. Add the following to the end of it:
```
[PipGUI]
enable = True
enable_shell = True
enable_editor = True
```
![???????????? ???????????? 2022-04-15 174232](https://user-images.githubusercontent.com/38569354/163572058-87acf0b3-0ade-4db5-ac3a-beb37ad00164.png)  
11. You're done! Now you can use package manager from IDLE!  

[:arrow_up:Table of contents](#Table-of-contents)
____
## Screenshots
![Example_screenshot_1](https://user-images.githubusercontent.com/38569354/162609212-2a1b9012-d36c-4c57-a911-d71ebe8297f1.png)
![Example_screenshot_2](https://user-images.githubusercontent.com/38569354/162609215-ddb8c09c-a9ec-4097-99e4-472b8cc79d6f.png)
![Example_screenshot_3](https://user-images.githubusercontent.com/38569354/162609217-64e30b5a-18d6-42fe-b773-cf0cd63e4a59.png)  

[:arrow_up:Table of contents](#Table-of-contents)
____
## FAQ
**Q:** Why doesn't it work?  
**A:** Maybe because I didn't test it thoroughly, maybe because you messed something up during an installation. In any case, feel free to open an issue with the following content:
1. Your Python version (e.g. 3.8)
2. Steps to reproduce your error (if you remember any)
3. Screenshot of an error message  

[:arrow_up:Table of contents](#Table-of-contents)
