-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true
-- Problem     Weather Observation Station 8
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-10-25, 05:58 p.m.
-- ──────────────────────────────────────────────────

/*
Enter your query here.
*/
 
SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(UPPER(CITY), 1) IN ('A', 'E', 'I', 'O', 'U')
  AND RIGHT(UPPER(CITY), 1) IN ('A', 'E', 'I', 'O', 'U');
