//The Query to Load the Stations in the Graph Database

LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/Williamdst/Capstone-2/main/Data/Stations-Decision-Points.csv' AS row
MERGE (s:Stations {name:row.stopName, ID:toInteger(row.stationID), borough:row.borough, lines:split(row.lines, ':'), nodes:split(row.nodes, ':')});


//The Query to Load the Relationships in the Graph Database

LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/Williamdst/Capstone-2/main/Data/Paths-Decision-Points.csv" AS row
MATCH (s1:Stations {ID:toInteger(row.startID)})
MATCH (s2:Stations {ID:toInteger(row.stopID)})
MERGE (s1)-[rel:LINK {routes:split(row.routes, ':'), start:split(row.startNode, ':'), stop:split(row.stopNode, ':')}]-(s2);

//The Query is the same, but in the file the headers are switched and modifications are made
//LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/Williamdst/Capstone-2/main/Data/Paths-Backward.csv" AS row
//MATCH (s1:Stations {ID:row.startID})
//MATCH (s2:Stations {ID:row.stopID})
//MERGE (s1)-[rel:LINK {routes:split(row.routes, ':'), cost:toInteger(row.distance)}]->(s2);

//Add Labels to the Nodes
MATCH (s1:Stations)
WHERE 'X1' in s1.lines
SET s1:X1;

MATCH (s1:Stations)
WHERE 'X2' in s1.lines
SET s1:X2;

MATCH (s1:Stations)
WHERE 'X3' in s1.lines
SET s1:X3;

MATCH (s1:Stations)
WHERE 'X4' in s1.lines
SET s1:X4;

MATCH (s1:Stations)
WHERE 'X5' in s1.lines
SET s1:X5;

MATCH (s1:Stations)
WHERE 'X6' in s1.lines
SET s1:X6;

MATCH (s1:Stations)
WHERE 'X7' in s1.lines
SET s1:X7;

MATCH (s1:Stations)
WHERE 'A' in s1.lines
SET s1:A;

MATCH (s1:Stations)
WHERE 'E' in s1.lines
SET s1:E;

MATCH (s1:Stations)
WHERE 'D' in s1.lines
SET s1:D;

MATCH (s1:Stations)
WHERE 'F' in s1.lines
SET s1:F;

MATCH (s1:Stations)
WHERE 'M' in s1.lines
SET s1:M;

MATCH (s1:Stations)
WHERE 'G' in s1.lines
SET s1:G;

MATCH (s1:Stations)
WHERE 'J' in s1.lines
SET s1:J;

MATCH (s1:Stations)
WHERE 'L' in s1.lines
SET s1:L;

MATCH (s1:Stations)
WHERE 'N' in s1.lines
SET s1:N;

MATCH (s1:Stations)
WHERE 'Q' in s1.lines
SET s1:Q;

MATCH (s1:Stations)
WHERE 'R' in s1.lines
SET s1:R;

MATCH (s1:Stations)
WHERE 'S' in s1.lines
SET s1:S;