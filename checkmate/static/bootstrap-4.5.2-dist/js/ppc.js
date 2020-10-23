function slice2Size(dataNum, dataTotal) {
  return (dataNum / dataTotal) * 360;
}
function addslice2(slice2Size, pieElement, offset, slice2ID, color) {
  $(pieElement).append("<div class='slice2 "+slice2ID+"'><span></span></div>");
  var offset = offset - 1;
  var sizeRotation = -179 + slice2Size;
  $("."+slice2ID).css({
    "transform": "rotate("+offset+"deg) translate3d(0,0,0)"
  });
  $("."+slice2ID+" span").css({
    "transform"       : "rotate("+sizeRotation+"deg) translate3d(0,0,0)",
    "background-color": color
  });
}
function iterateslice2s(slice2Size, pieElement, offset, dataCount, slice2Count, color) {
  var slice2ID = "s"+dataCount+"-"+slice2Count;
  var maxSize = 179;
  if(slice2Size<=maxSize) {
    addslice2(slice2Size, pieElement, offset, slice2ID, color);
  } else {
    addslice2(maxSize, pieElement, offset, slice2ID, color);
    iterateslice2s(slice2Size-maxSize, pieElement, offset+maxSize, dataCount, slice2Count+1, color);
  }
}
function createPie(dataElement, pieElement) {
  var listData = [];
  $(dataElement+" span").each(function() {
    listData.push(Number($(this).html()));
  });
  var listTotal = 0;
  for(var i=0; i<listData.length; i++) {
    listTotal += listData[i];
  }
  var offset = 0;
  var color = [
    "#93898C",
    "#D37489"
  ];
  for(var i=0; i<listData.length; i++) {
    var size = slice2Size(listData[i], listTotal);
    iterateslice2s(size, pieElement, offset, i, 0, color[i]);
    $(dataElement+" li:nth-child("+(i+1)+")").css("border-color", color[i]);
    offset += size;
  }
}
createPie(".pieID2.legend2", ".pieID2.pie2");
