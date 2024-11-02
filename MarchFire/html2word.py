from py_mini_racer import py_mini_racer

js_code = """
var fs = require('fs');
var htmlDocx = require('html-docx-js');

var html = '<h1>Hello World</h1><p>This is a paragraph.</p>';  // Replace this with your HTML content
var docx = htmlDocx.asBlob(html);

fs.writeFileSync('test.docx', docx);
"""

ctx = py_mini_racer.MiniRacer()
ctx.eval(js_code)