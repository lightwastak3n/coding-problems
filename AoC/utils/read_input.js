const fs = require('fs');


function processData(filePath, cb) {
	fs.readFile(filePath, 'utf8', (err, data) => {
		if (err) {
			console.log(err)
			return;
		}
		cb(data);
	});
}

module.exports = processData;
