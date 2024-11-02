var officegen = require('officegen');
var fs = require('fs');

var docx = officegen('docx');

var pObj = docx.createP();

pObj.addText('Hello World');
pObj.addText('This is a paragraph.', { breakLine: true });

var out = fs.createWriteStream('test.docx');

out.on('error', function(err) {
  console.log(err);
});

docx.generate(out);