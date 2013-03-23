var nn = require('../build/Release/nodetime_native.node');


var start = nn.time();
var startCpu = nn.cpuTime();
console.time('date');

setTimeout(function() {
  for(var i = 0; i < 1000000; i++) {
    nn.time();
    nn.cpuTime();
  }

  console.timeEnd('date');
  console.log('time', nn.time() - start);
  console.log('cpuTime', nn.cpuTime() - startCpu);
  console.log(nn.cpuTime(), nn.time())
}, 3000);



function test3(count) {
  if(count < 10000) {
    test3(count + 1)
  }
  
  var b = 3 + 4;
}

function test2() {
  var a = 1 + 2;
}

function test1() {
  test3(0);

  for(var i = 0; i < 100000000; i++) {
    test2();
  }

}

test1();


