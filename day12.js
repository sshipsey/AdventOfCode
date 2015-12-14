fs = require('fs');
var total = 0;

function day12(input) {
  jsonObject = JSON.parse(input);
  console.log(iterateObject(jsonObject));
}

function iterateObject(object) {
  for (var key in object) {
    if (hasRed(object)) {
      break;
    }
    if (typeof(object[key]) == 'object') {
      iterateObject(object[key]);
    } else {
      if (!isNaN(object[key])) {
        total += Number(object[key]);
      }
    }
  }
  return total;
}
function hasRed(object) {
  for (var key in object) {
    // For arrays, we don't care if they have red
    if (Array.isArray(object)) {
      return false;
    }
    // For objects, we do
    if (object[key] == "red") {
      return true;
    }
  }
  return false;
}
jsonData = fs.readFile('C:\\Development\\AdventOfCode\\inputs\\day12.txt', 'utf8', function(err, data) {
  if (err) {
    return console.log(err);
  } else {
    return day12(data);
  }
});