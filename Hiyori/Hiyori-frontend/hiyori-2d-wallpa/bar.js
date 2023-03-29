 'use strict';

var bars = [];
var baseOrigin;
var baseAngle;
let audioData = engine.registerAudioBuffers(64);

/**
 * @param {Boolean} value (for property 'visible')
 */
export function update() {
    var origin = baseOrigin.copy();
    var scale = new Vec3(2.5); /* edit this value for bar width, for horizontal 6 for vertical 3*/

    for (var i = 0; i < 64; ++i) {
        let amt = audioData.average[i];
        let bar = bars[i];

        scale.y = amt * 80;
        origin.x += 30; /*edit this value for horizontal bar spacing, for horizontal bar 30 for vertical 0*/
        origin.y += 0; /*edit this value for Vertical bar spacing, for Vertical bar 17 for horizontal 0 */
        bar.scale = scale;
        bar.origin = origin;

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
        let angle = 360 * (i / 64);
        let bar = bars[i];
        bar.angles = new Vec3(0, 0, 0); /* this controls bar rotation, the 3rd value is the rotation to change, for horizontal bar 0 for vertical 90*/


    }
    baseOrigin = thisLayer.origin;

}
//960, 540//from getSource.py