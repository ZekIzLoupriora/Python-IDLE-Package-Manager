# Python IDLE Package Manager
A simple package manager extension with GUI for the default Python IDLE
____
## Installation
0. Install dependencies:
```
pip install PyQt5 urllib3 requests lxml
```
or using **req.txt** file (preferred):
```
pip install -r req.txt
```
1. Clone this repo or download it as a ZIP archive;
2. Open your Python installation directory (it is usually located at /path/to/your/user/folder/AppData/Local/Programs/Python/PythonXX-YY);
3. Put the **PipGUI.py** and **PacMan** folder into the **/Lib/idlelib/** directory; it should look something like this:  
![Снимок экрана 2022-04-10 125829](https://user-images.githubusercontent.com/38569354/162608531-7514bc24-77c8-4001-a961-8a33a08d9d41.png)
![Снимок экрана 2022-04-10 125801](https://user-images.githubusercontent.com/38569354/162608515-82859375-1a3a-4abd-9e18-f94d7485bc9b.png)
4. Locate the **editor.py** file in the **/Lib/idlelib/** directory and open it with the text editor of your choice;
5. Search for **menu_specs**; it should look something like this:
![Снимок экрана 2022-04-10 130146](https://user-images.githubusercontent.com/38569354/162608639-a7a993f7-937f-4144-a925-d71880512453.png)
6. Add the following line to the end of this list: **```("pacman", "Pac_Man"),```**  
Now it should look like this:  
![Снимок экрана 2022-04-10 130524](https://user-images.githubusercontent.com/38569354/162608794-0229287c-a5d7-474a-a5db-7a0a2d90d81b.png)
7. **Optional:** Do steps 4-6 with the **pyshell.py** file (if you don't, you will not see **PacMan** menu entry while running scripts via IDLE);
8. You're done! Now you can use package manager from IDLE!
____
## Screenshots
![Example_screenshot_1](https://user-images.githubusercontent.com/38569354/162609212-2a1b9012-d36c-4c57-a911-d71ebe8297f1.png)
![Example_screenshot_2](https://user-images.githubusercontent.com/38569354/162609215-ddb8c09c-a9ec-4097-99e4-472b8cc79d6f.png)
![Example_screenshot_3](https://user-images.githubusercontent.com/38569354/162609217-64e30b5a-18d6-42fe-b773-cf0cd63e4a59.png)
