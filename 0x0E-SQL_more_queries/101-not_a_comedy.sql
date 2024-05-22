-- not
-- comedy
SELECT tv_shows.title
FROM tv_shows
WHERE NOT EXISTS (
    SELECT 1
    FROM tv_show_genres
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_show_genres.show_id = tv_shows.id
    AND tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
