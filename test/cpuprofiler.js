var nn = require('../build/Release/nodetime_native.node');


nn.startV8Profiler();

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

nn.stopV8Profiler(function(parentNodeUid, nodeUid, totalSamplesCount, functionName, scriptResourceName, lineNumber) {
  console.log(parentNodeUid, nodeUid, totalSamplesCount, functionName, scriptResourceName, lineNumber);
});


