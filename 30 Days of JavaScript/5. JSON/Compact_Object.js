/**
 * @param {Object} obj
 * @return {Object}
 */
var compactObject = function(obj) {
    if (obj===null) return null;
    if (typeof obj != 'object') return obj;
    if (Array.isArray(obj)) return obj.filter(Boolean).map(compactObject)
    // .map(fn) applies fn to all elements. This provides recursive call of fn on array here. 

    Object.keys(obj).forEach(element => {
        if (!(obj[element])) delete obj[element];
        else obj[element]= compactObject(obj[element]);
    })
    return obj;
};
