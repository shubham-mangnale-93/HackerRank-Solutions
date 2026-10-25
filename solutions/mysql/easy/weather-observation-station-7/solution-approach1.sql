-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true
-- Problem     Weather Observation Station 7
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-10-25, 05:41 p.m.
-- ──────────────────────────────────────────────────

/*
Enter your query here.
*/
SELECT DISTINCT CITY
FROM STATION
WHERE UPPER(CITY) LIKE '%A'
   OR UPPER(CITY) LIKE '%E'
   OR UPPER(CITY) LIKE '%I'
   OR UPPER(CITY) LIKE '%O'
   OR UPPER(CITY) LIKE '%U';
