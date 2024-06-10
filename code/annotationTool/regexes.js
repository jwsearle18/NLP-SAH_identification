var regex_names = {
  "a": "Positive",
  "b": "Negative",
  "c": "Keywords"
};

var colors = {
  "a": "#ff0000",
  "b": "#ffff00",
  "c": "#ffc0cb"
};
var regexes = {
  "a": [
  /\bSAH\b/gmi, 
  /subarachnoid hemorrhage/gmi,
  /\bcoil/gmi,
  /\bclip/gmi,
  /nimodipine/gmi,
  /stroke/gmi,
  /nontraumatic/gmi,
  /aneurysm/gmi,
  /subarachnoid/gmi,
  /hemorrhage/gmi,
  /neck/gmi,
  /xanthochromia/gmi,
  /\bcsf\b/gmi,
  /brain bleed/gmi,
  /bleed/gmi
  ],
  "b": [
  /trauma/gmi,
  /no hemorrhage/gmi,
  /\bfell\b/gmi,
  /\bfall\b/gmi,
  /\bhit\b/gmi,
  /\btbi\b/gmi,
  /without hemorrhage/gmi,
  /w\/o hemorrhage/gmi
  ],
  "c": [
  /admission diagnosis/gmi,
  /principal problem/gmi,
  /surgeries/gmi,
  /etiology/gmi,
  /discharge instructions/gmi,
  /hospital course/gmi
  ]
};



function createDivsAndRules(regexes, colors, regex_names) {
  var row = document.getElementById('row');

  var style = document.createElement('style');
  style.appendChild(document.createTextNode(""));
  document.head.appendChild(style);

  var stylesheet = style.sheet;

  Object.entries(regexes).forEach(([key, regexArr], index) => {
    var className = "class_" + key;

    // Convert hexadecimal color to RGBA and decrease the opacity
    var color = colors[key];
    var rgbaColor = "rgba(" + parseInt(color.slice(1, 3), 16) + ", " 
      + parseInt(color.slice(3, 5), 16) + ", " 
      + parseInt(color.slice(5, 7), 16) + ", 0.5)";

    // Add a new CSS rule for this class for div elements, setting the background color with decreased opacity
    var ruleForDiv = "div." + className + " { background-color: " + rgbaColor + "; border: 1px solid "+color+" }";
    stylesheet.insertRule(ruleForDiv, stylesheet.cssRules.length);

    // Add a new CSS rule for this class for mark elements, setting the background color without changing opacity
    var ruleForMark = "mark." + className + " { background-color: " + color + "; }";
    stylesheet.insertRule(ruleForMark, stylesheet.cssRules.length);

    var newDiv = document.createElement("div");
    newDiv.className = "col " + className;
    row.appendChild(newDiv);

    // Add a rule based on the regex_names array
    var ruleForRegexName = "div." + className + "::before { content: '" + regex_names[key] + ":\n\n'; white-space: pre; }";
    stylesheet.insertRule(ruleForRegexName, stylesheet.cssRules.length);
  });
}


setTimeout(() => {createDivsAndRules(regexes, colors,regex_names)}, 500);
	
	
