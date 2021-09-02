-- Ranks country origins of bands, ordered by number of fans
-- origin: country of origin
-- nb_fans: number of fans
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
