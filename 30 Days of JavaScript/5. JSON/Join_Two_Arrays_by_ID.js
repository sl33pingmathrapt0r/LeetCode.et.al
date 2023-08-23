/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    joinedObj= {}
    for (el of arr2) {
        // all of arr2 guaranteed to be included
        joinedObj[el["id"]]=el;
    }
    for (el of arr1) {
        // 'in' operator checks for private property id
        // => 'in' checks for index in arrays. 
        // use .includes() for arrays
        if (!(el["id"] in joinedObj)) joinedObj[el["id"]]=el;
        else {
            for (key in el) {
                if (! (key in joinedObj[el["id"]]) ) 
                    joinedObj[el["id"]] [key]= el[key];
            }
        }
    }

    return Object.values(joinedObj).sort((a,b) => a["id"] - b["id"]);
};
