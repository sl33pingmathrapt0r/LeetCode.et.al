(
  SELECT name AS results
  FROM Users
  LEFT JOIN MovieRating ON Users.user_id=MovieRating.user_id
  GROUP BY Users.user_id
  ORDER BY COUNT(rating) DESC, name
  LIMIT 1
)
UNION ALL
(
  SELECT title as results
  FROM Movies
  LEFT JOIN MovieRating ON Movies.movie_id=MovieRating.movie_id
  WHERE created_at BETWEEN "2020-02-01" AND "2020-02-29"
  GROUP BY Movies.movie_id
  ORDER BY AVG(rating) DESC, title
  LIMIT 1
);
