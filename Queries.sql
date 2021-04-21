//The Query to Load the Stations in the Graph Database

LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/Williamdst/Capstone-2/main/Data/Stations-Subset.csv' AS row
MERGE (s:Stations {name:row.stopName, ID:row.stationID, borough:row.borough, routes: split(row.routes, ':'), nodes: split(row.nodes, ':')});


//The Query to Load the Relationships in the Graph Database

LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/Williamdst/Capstone-2/main/Data/Paths-Forward.csv" AS row
MATCH (s1:Stations {ID:row.startID})
MATCH (s2:Stations {ID:row.stopID})
MERGE (s1)-[adj:Adjacent]->(s2);

//The Query is the same, but in the file the headers are switched and modifications are made
//LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/Williamdst/Capstone-2/main/Data/Paths-Backward.csv" AS row
//MATCH (s1:Stations {ID:row.startID})
//MATCH (s2:Stations {ID:row.stopID})
//MERGE (s1)-[adj:Adjacent]->(s2);

//Add Labels to the Nodes
MATCH (s1:Stations)
WHERE 'A' in s1.routes
SET s1:A;

MATCH (s1:Stations)
WHERE 'E' in s1.routes
SET s1:E;

MATCH (s1:Stations)
WHERE 'J' in s1.routes
SET s1:J;

MATCH (s1:Stations)
WHERE 'L' in s1.routes
SET s1:L;

-------------------------------------

// Query to run minimum spanning tree
MATCH (n:Stations {ID: '209'})
CALL gds.alpha.spanningTree.minimum.write({
    nodeProjection:'Stations',
    relationshipProjection: { 
        LINK: {
            type: 'Adjacent',
            orientation: 'UNDIRECTED'
        }
    },
    startNodeId: ID(n),
    writeProperty: 'MINST',
    weightWriteProperty: 'writeCost'
})
YIELD createMillis, computeMillis, writeMillis, effectiveNodeCount
RETURN createMillis, computeMillis, writeMillis, effectiveNodeCount




// Query to return the start and stop 
WITH relationships(path) as rels
UNWIND rels as rel
with distinct rel as rel
return startNode(rel).ID AS source, endNode(rel).ID AS destination, rel.writeCost AS cost