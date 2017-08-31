/*

Check to see if the user has Docker installed and which version of Python they prefer.

*/

'use strict';
var inquirer = require('inquirer');
var YAML = require('js-yaml');
var fs = require('fs');

console.log('Hi, a few quick questions before we start:');

var questions = [
  {
    type: 'list',
    name: 'python',
    message: 'What Python version?',
    choices: ['python2.7', 'python3.6'],
    filter: function (val) {
      return val.toLowerCase();
    }
  },
  {
    type: 'confirm',
    name: 'docker',
    message: 'Do you have Docker installed? Recommended, but not required.',
    default: true
  },
]

inquirer.prompt(questions).then(function (answers) {
  
  var doc = YAML.safeLoad(fs.readFileSync('serverless.yml', 'utf8'));
  doc.custom.pythonRequirements.dockerizePip = answers.docker;
  doc.provider.runtime = answers.python;
  fs.writeFileSync('serverless.yml', YAML.dump(doc));
});
