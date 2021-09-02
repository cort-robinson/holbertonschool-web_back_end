-- Lists all bands with Glam rock as their main style, ranked by longevity
-- Column names must be: band_name and lifespan
-- Use attributes formed and split for computing lifespan
SELECT band_name, (IFNULL(split, 2021) - formed) AS lifespan
FROM metal_bands WHERE style = 'Glam Rock'
