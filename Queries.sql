--The Query to Load the Stations in the Graph Database

LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/Williamdst/Capstone-2/main/Data/Stations-Subset.csv' AS row fieldterminator ','
MERGE (s:Stations {name:row.stopName, ID:row.stationID, borough:row.borough, routes: split(row.routes, ':'), nodes: split(row.nodes, ':')})


--The Query to Load the Relationships in the Graph Database

LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/Williamdst/Capstone-2/main/Data/Paths.csv" AS row
match (s1:Stations {ID:row.startID})
match (s2:Stations {ID:row.stopID})
merge (s1)-[adj:Adjacent]->(s2)