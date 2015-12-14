fs = require('fs');

function day12(input) {
  jsonObject = JSON.parse(input);
  iterateObject(jsonObject);
}
function iterateObject(object) {
  for (var key in object) {
    // Implement a BFS for this json "tree" to parse all values
    // It's weird because some are arrays and some are objects.
    // Maybe we can flatten this somehow?
    console.log(key + " " + object[key].length);
  }
}

jsonData = fs.readFile('C:\\Development\\AdventOfCode\\inputs\\day12.txt', 'utf8', function(err, data) {
  if (err) {
    return console.log(err);
  } else {
    return day12(data);
  }
});