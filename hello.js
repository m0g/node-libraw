var addon = require('./build/Release/addon');

console.log(addon.hello());
console.log(addon.add(3,5));

addon.runCallback(function(msg) {
  console.log(msg);
})

var obj1 = addon.createObject('hello obj1');
var obj2 = addon.createObject('world');

console.log(obj1.msg+' '+obj2.msg); // 'hello world'

var fn = addon.createFunction();

console.log('fn', fn());
