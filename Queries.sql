--The Query to Load the Stations in the Graph Database

LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/Williamdst/Capstone-2/main/Data/Stations-Subset.csv' AS row fieldterminator ','
MERGE (s:Stations {name:row.StopName, ID:row.StationID, borough:row.Borough, routes: split(row.Routes, ':'), nodes: split(row.Nodes, ':')})