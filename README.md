# PS1-VBB
![Cocoapods platforms](https://img.shields.io/badge/Plaform-linux%20%7C%20osx-green)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
### Need to be used in conjunction with [GMeetRecorder by Alexandre P J](https://github.com/Alexandre-P-J/GMeetRecorder)
Scripting of GMeetRecorder such that it automatically joins and records google meets scheduled in your google calendar
## Go to [Google Apps Script](https://script.google.com/home/start)
1. Create a new Project
2. Change the code in the editor i.e.
	> Replace the code in the editor, which is currently
	```javascript
	function myFunction() {

		}
	```
	> With the code in **GoogleAppScript.js** file present in this repository
3. Next add **Services** to this Apps Script Project. We are employing Calendar and Sheet API in this project, so add them under services.
4.	Make a Google Sheet with default sheet being *Sheet1* and add column headings as given in code.
**OR**
	 You can just make a copy of this [GSheet](https://docs.google.com/spreadsheets/d/1TpwFSYhljJUBLa1iBwYTDBpFtWVIPa3LxZegawDk01Q/edit?usp=sharing)
5. Lastly, you need to edit the myFunction(or the code you just pasted). Add your *calendarId* and *spreadsheetId*. Follow comments given in the code
6. **Remember to use the CalendarId and SpreadsheetId owned by the same gmail account you used to create the Apps Script**. You can make further changes such as changing the number of events, addition of another column of details like end time of meets, etc.
7. Run the code by using the **Run** button present on the top panel in the Editor pane
8. During the first run, a pop-up will open, login with the same gmail account and give permission for the Apps Script to edit your spreadsheet and calendar
9. Add Trigger to this Apps Script by clicking on the **Trigger** button present on the left panel so that it runs automatically and mails a report incase of execution failure

## Get a service account
1. Create a new project under [Google Cloud Platform](https://console.cloud.google.com/projectselector2/home/dashboard?supportedpurview=project)
2 Give it a name (such as, automating-meetbot) and then under **Getting Started**, select **Explore and Enable APIs**
3. Add Google Sheet API
4. Search for **Service Account** in the top search bar and click the link with **IAM & Admin** as its description
5. Create a service account, and give it a role to access resources. ( Needs further research - I went with Owner as the role)
6. Create a key for this account by clicking under the button under **Actions** and selecting *Manage Keys*
7. Add  a key and download, store the Json file securely on the system/server or you can even create a json key and then upload it to the service account.
8. Name the json file as key.json and store it in the folder of the repository or link its address properly in the script.py
9. Finally, do share the GSheet with the email address of your service account, and keep note of service account email address.
10. Incase you find the instructions difficult to follow, you can read and follow up from [here](https://docs.gspread.org/en/v3.7.0/oauth2.html#for-bots-using-service-account)

## Edit Script.py
1. Install the python library *gspread* by using the following command in your terminal. You may install this library globally by using sudo as the prefix
	```shell
	pip install gspread
	```
2. Now in the script.py file edit the code as per your personal preference by following the comments. **Importantly,**
	* Add the path to your service account json file
	* Add the spreadsheet Id
	* Location to the GMeetRecorder directory to store the script
	* Directory where you want to store the recordings
4. You may automate this script to run at certain interval depending on your usage using cronjobs or any other software of your choice

