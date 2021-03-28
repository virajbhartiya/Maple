function doGet(e) {
  sheet = "1pvd4hTR8WElcEL36k9lfsubjXxK9O_19GCjTiNKkotY";
  sheetId = sheet;
  response = "10";
  try {
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    cols = ["", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    key = e.parameter.key;
    names = e.parameter.names;
    roll = e.parameter.roll;
    time = e.parameter.time;

    month = new Date().getMonth();
    date = new Date().getDate() + 1
    try {
      sheet = SpreadsheetApp
        .openById(sheet).getSheetByName(months[month]);
    } catch (ex) {
      insertData = ["Name", "Roll"];
      sheet = SpreadsheetApp.openById("1pvd4hTR8WElcEL36k9lfsubjXxK9O_19GCjTiNKkotY")

      sheet.insertSheet().setName(months[month])
      for (i = 0; i < 8; i++) {
        sheet.insertColumnAfter(3);
      }
      cell = sheet.getRange("A1")
      cell.setValue(insertData[0])
      cell.setFontWeight("bold")

      cell = sheet.getRange("B1")
      cell.setValue(insertData[1])
      cell.setFontWeight("bold")

      sheet.setFrozenRows(1);
      sheet.setFrozenColumns(2)
    }
    if (key == "update") {
      response = names

      roll = roll.substring(1)
      names = names.split(",")
      roll = roll.split(",")
      time = time.split(",")

      day = cols[date - 1]
      cell = sheet.getRange(day + "1")
      cell.setValue(date - 1)
      cell.setFontWeight("bold")

      var data = sheet.getDataRange().getValues();

      for (i = 0; i < names.length; i++) {
        for (j = 0; j < 50; j++) {
          try {
            if (data[j][0] == names[i]) {
              cell = sheet.getRange(day + (j + 1))
              cell.setValue(time[i])
              break
            }
          } catch (ex) {
          }
        }

      }
      sheet.sort(2)
    }



    else if (key == "create") {
      names = names.split(",")
      roll = roll.split(",")

      sheet = SpreadsheetApp.openById("1pvd4hTR8WElcEL36k9lfsubjXxK9O_19GCjTiNKkotY").getSheetByName(months[month])
      var data = sheet.getDataRange().getValues();

      for (i = 0; i < names.length; i++) {
        names[i] = names[i].substring(names[i].indexOf('\'') + 1, names[i].lastIndexOf('\''));
        roll[i] = roll[i].substring(roll[i].indexOf('\'') + 1, roll[i].lastIndexOf('\''));
      }
      for (i = 0; i < names.length; i++) {
        update = true
        for (j = 1; j < data.length; j++) {
          if (data[j][0] == names[i]) {
            update = false
            break
          }
        }
        if (update) {
          var rowDate = sheet.appendRow([names[i], roll[i]]);
        }
      }
      sheet.sort(2);
      response = 0
    }

  } catch (ex) {
    response = -1
  }
  return ContentService.createTextOutput(JSON.stringify(response)).setMimeType(ContentService.MimeType.JSON);
}
