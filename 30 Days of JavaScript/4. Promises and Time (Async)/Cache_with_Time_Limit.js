var TimeLimitedCache = function() {
    // new class allows getting and setting key-value pairs, 
    // however a time until expiration is associated with each key. 
    this.timeouts= {};
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let inBool= false; 
    if (key in this.timeouts) {
        inBool= true;
        clearTimeout(this.timeouts[key].timeout);
    }

    // store timeout ref together w key
    this.timeouts[key]= {
        value, // same as value:value
        timeout: setTimeout( ()=> delete this.timeouts[key], duration)
    };
    return inBool;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (key in this.timeouts) return this.timeouts[key].value;
    return -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.timeouts).length;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */
