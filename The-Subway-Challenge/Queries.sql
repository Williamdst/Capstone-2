//The Query to Load the Stations in the Graph Database

LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/Williamdst/Capstone-2/main/Data/Stations-Decision-Points.csv' AS row
MERGE (s:Stations {name:row.stopName, ID:toInteger(row.stationID), borough:row.borough, lines: split(row.lines, ':'), nodes: split(row.nodes, ':')});


//The Query to Load the Relationships in the Graph Database

LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/Williamdst/Capstone-2/main/Data/Paths-Decision-Points.csv" AS row
MATCH (s1:Stations {ID:toInteger(row.startID)})
MATCH (s2:Stations {ID:toInteger(row.stopID)})
MERGE (s1)-[rel:LINK {routes:split(row.routes, ':')}]-(s2);

//The Query is the same, but in the file the headers are switched and modifications are made
//LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/Williamdst/Capstone-2/main/Data/Paths-Backward.csv" AS row
//MATCH (s1:Stations {ID:row.startID})
//MATCH (s2:Stations {ID:row.stopID})
//MERGE (s1)-[rel:LINK {routes:split(row.routes, ':'), cost:toInteger(row.distance)}]->(s2);

//Add Labels to the Nodes
MATCH (s1:Stations)
WHERE 'X1' in s1.lines
SET s1:One;

MATCH (s1:Stations)
WHERE 'X2' in s1.lines
SET s1:Two;

MATCH (s1:Stations)
WHERE 'X3' in s1.lines
SET s1:Three;

MATCH (s1:Stations)
WHERE 'X4' in s1.lines
SET s1:Four;

MATCH (s1:Stations)
WHERE 'X5' in s1.lines
SET s1:Five;

MATCH (s1:Stations)
WHERE 'X6' in s1.lines
SET s1:Six;

MATCH (s1:Stations)
WHERE 'X7' in s1.lines
SET s1:Seven;

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

-------------------------------------

// Query to run minimum spanning tree
MATCH (n:Stations {ID: 209})
CALL gds.alpha.spanningTree.minimum.write({
    nodeProjection:'Stations',
    relationshipProjection: { 
        LINK: {
            type: 'LINK',
			properties: 'cost',
            orientation: 'UNDIRECTED'
        }
    },
    startNodeId: ID(n),
	relationshipWeightProperty: 'cost',
    writeProperty: 'MINST',
    weightWriteProperty: 'writeCost'
})
YIELD createMillis, computeMillis, writeMillis, effectiveNodeCount
RETURN createMillis, computeMillis, writeMillis, effectiveNodeCount




// Query to return the start and stop 
MATCH path = (s:Stations {ID: 209})-[:MINST*]-()
WITH relationships(path) as rels
UNWIND rels as rel
with distinct rel as rel
return startNode(rel).ID AS source, endNode(rel).ID AS destination, rel.writeCost AS cost