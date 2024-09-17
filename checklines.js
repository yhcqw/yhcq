const fs = require('fs');

// Read the file
fs.readFile('updated_new.txt', 'utf8', (err, data) => {
  if (err) throw err;

  // Split the file content into lines
  const lines = data.split('\n');

  // Check each line for "作者"
  lines.forEach((line, index) => {
    if (!line.includes('作者')) {
      console.log(`Line ${index + 1}: ${line}`);
    }
  });
});
