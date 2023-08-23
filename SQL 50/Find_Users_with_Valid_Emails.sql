SELECT * 
FROM Users
WHERE mail REGEXP '^[A-Za-z][\\w\.\-]*@leetcode(\\?com)?\\.com$';
-- -\w means alphanumeric and underscore
-- -(\\? XX )?\\ means WTF
