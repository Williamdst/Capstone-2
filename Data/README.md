<h3>Paths-Decision-Points</h3>
The complete edgelist of the MTA Subway System. Modeling the edges was similar to modeling the stations. When modeling stations, each row is a single station and the properties of that station. When modeling edges, each row is a single edge and the properties of that edge. Edges are defined by the two nodes it is connected to, so the first thing needed are the Start Station ID and the Stop Station ID. The three other properties were the routes (same idea as the "lines" column), the nodes (the node numbers), and the distance. In this case, the distance was the <b>time</b> it takes to traverse the edge, or in other words, the time to go from one station to the next. The edge that connects Canal St to W 4 St-Wash Sq is shown below:
 <table>
        <tr>
            <th>startID</th>
            <th>stopID</th>
            <th>startNode</th>
            <th>stopNode</th>
            <th>routes</th>
            <th>distance</th>
        </tr>
        <tr>
            <td>169</td>
            <td>167</td>
            <td>A010:E009</td>
            <td>A011:E008</td>
            <td>A:E</td>
            <td>4</td>
        </tr>
    </table>
Although you can traverse this edge on either the A or E train, it is important that this edge is <b>not</b> duplicated in the edge list. If the edge is duplicated, then the program will read it as two separate edges and will solve the problem under the impression that it must traverse the edge twice. After removing all the duplicates there were 104 edges modeled. <br></br>


<b>Paths-Decision-Points-Subset</b><br />
A simplified subset of the edgelist. The lines modeled are the A,E,J,L trains <br />

<b>Paths-Matching-Test</b><br />
A super simple edgelist that can be used for testing the program and deciphering what is happening. This edgelist was used in the report to explain the program.


<h3>Stations-Decision-Points</h3>
The 79 stations where the challenger needs to make a decision

Stations-Official-472
The list of all 472 stations needed to complete the challenge. For example Broadway Junction, although
a single point on the map is considered three different stations. One for the A/C, the L, and J/Z trains. 

Stations-Raw
The raw station data provided by the MTA website.
