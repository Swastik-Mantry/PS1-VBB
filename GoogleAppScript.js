function myFunction() {

	//EDIT BELOW THIS --->

	let calendarId = 'johndoepersonal@gmail.com'; //Usually the Email-ID. Need to check/get the CalenderID ?-->Google "how to get the calendarID"
	let spreadsheetId = '1XEAjWLI7i6M-TYuKK_gjErV-AxO9O9EDZeqavhGuys456'; // Add your Spreadhseet Id, Visit this link to understand https://developers.google.com/sheets/api/guides/concepts

	//Number of events you want to script to fetch each time, Need to edit the Range incase of changes here i.e. need to edit "Sheet1!XX:YY" such that XX, YY span those many rows
	let no_of_events = 20;

	//<--- EDIT ABOVE THIS

	//DO NOT EDIT BELOW THIS UNTIL YOU KNOW WHAT YOU ARE DOING
	//***Incase of changing the number of Columns under usage on the GSheet, need to add more "" in deletion***
	//Fetching the events from the Calendar API

	//Current Date
	let now = new Date();

	//Actual Fetch
	let events = Calendar.Events.list(calendarId, {
		timeMin: now.toISOString(),
		singleEvents: true,
		orderBy: 'startTime',
		maxResults: no_of_events
	});

	//Storing in the form of a list as per Google Sheet API 'Write' documentation
	let values = [];
	for(let i = 0; i < no_of_events; i += 1)
		values[i] = ["", "", "", ""];

	//Deleting previous values
	let emptyRange = Sheets.newValueRange();
	emptyRange.values = values;
	let response = Sheets.Spreadsheets.Values.update(emptyRange, spreadsheetId, "Sheet1!A2:D22", {
		valueInputOption: "RAW"
	});

	//GSheet Columns and data
	if (events.items && events.items.length > 0) {
		for (var i = 0; i < events.items.length; i++) {
			let event = events.items[i];
			values[i] = [(i + 1), event.start.dateTime, event.summary, event.hangoutLink]; //[Serial No.][Time][Title of the Event][Meet Link]
		}
	} else {
		Logger.log('No events found.');
	}

	//Updating New values Everytime
	let valueRange = Sheets.newValueRange();
	valueRange.values = values;
	let result = Sheets.Spreadsheets.Values.update(valueRange, spreadsheetId, "Sheet1!A2:D22", {
		valueInputOption: "RAW"
	});

}
