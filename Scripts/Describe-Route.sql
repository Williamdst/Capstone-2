-- To find the stations for a route change the first WHERE clause to desired path
-- Path 416 - 378 is shown.
WITH RECURSIVE split(path, route, str) AS(
    SELECT
      path,
      '',
      route||'-'
    FROM routes
    WHERE path = '416 - 378'

    UNION SELECT
      path,
      substr(str,0, instr(str, '-')),
      substr(str, instr(str,'-')+1)
    FROM split
    WHERE str!='-'
)
SELECT
  path,
  route,
  station
FROM split
INNER JOIN stations
  ON split.route = stations.stationid
