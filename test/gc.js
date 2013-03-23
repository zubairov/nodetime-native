var nn = require('../build/Release/nodetime_native.node');

nn.afterGC(function(gcType, gcFlags, usedHeapSize) {
  console.log('GC Type', gcType);
  console.log('GC Flags', gcFlags);
  console.log('Used Heap Size', usedHeapSize);
});

setInterval(function() {
  for(var i = 0; i < 1000; i++) {
    new Object();
  }
}, 2000);

