 'use strict';
var bars = [];
var baseOrigin;
let audioData = engine.registerAudioBuffers(64);
let timerFlag = true;
let sceneFlag = false;

var reference;

function timeCalculator(delta){
	let t = engine.timeOfDay * 100000;
	if (timerFlag == true){
		timerFlag = false;
		reference = t;
        if (sceneFlag == true){
            sceneFlag = false;
        }
        else if (sceneFlag != true){
            sceneFlag = true;	
        }
        
	}
	let timer = t - reference;

	if (timer > delta){
		timerFlag = true;
        
	}
    
}


/**
 * @param {Boolean} value (for property 'visible')
 */
export function update() {
	timeCalculator(Math.floor(Math.random() * 4500) + 1);
    var origin = baseOrigin.copy();
    var scale = new Vec3(2.5); 

    for (var i = 0; i < 64; ++i) {
        let amt = audioData.average[i];
        let bar = bars[i];
        
        if (amt == 0 && !sceneFlag){
        scale = 1;
        bar.scale = scale;
        }
        else{
            bar.scale = 0;
        }
    }
}

/**
 * @param {Boolean} value (for property 'visible')
 */
export function init() {
    bars.push(thisLayer);
    let thisIndex = thisScene.getLayerIndex(thisLayer);
    for (var i = 1; i < 64; ++i) {
        let newBar = thisScene.createLayer('models/bar.json');
        thisScene.sortLayer(newBar, thisIndex);
        newBar.parallaxDepth = new Vec2(0, 0);
        bars.push(newBar);
    }

    for (var i = 0; i < 64; ++i) {

        let bar = bars[i];
        bar.angles = new Vec3(0, 0, 0); 


    }
    baseOrigin = thisLayer.origin;

}//from getSource.py