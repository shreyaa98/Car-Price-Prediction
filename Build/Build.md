1) Make sure you have python 3.12.1 (should be the latest version) on your local pc or laptop. (Be sure to uninstall other python versions too if you have,better to start fresh)
   (Note: during installation, uncheck the first box for install with admin priviledge but check for the second box - Add python to path, the rest just follow through the process with default option)

2) After python installation, go to windows -> settings -> Apps -> Advanced Apps Settings -> App Execution aliases -> Both App Installer [python/python3] (set to off) 

3) go to powershell , type "python -V" , to check if the python version is displayed, and also type "pip -V" , you should see something similar [pip 23.2.1 from C:\Users\XXX\AppData\Local\Programs\Python\Python312\Lib\site-packages\pip (python 3.12)] , if both of these displayed correctly, then installation is going smoothly which is good.

4) again go to powershell, type "cd /path..."  , type "pip install -r .\requirements.txt" , wait for library installation to finish.

5) To run the application , type "python .\carAnalysisApp.py"  , or type "pytest .\testCarAnalysisApp.py --cov=carAnalysisApp --cov-report=xml" to run unit tests and generate report.
