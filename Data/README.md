<div>
    <h2 align='center'> The Line on the Night Map are Grouped Into Colors </h2>
</div>

<img align='right' width='400' style="float:right;" src="https://raw.githubusercontent.com/Williamdst/Capstone-2/main/Images/0007.MTA-Night.jpg" />

<div style="text-align:center;margin:0;font-size:12px;color:#c1121f" align='center'>
    <table>
    <tr>
        <th>Red Lines</th>
        <td>1</td>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <th>Green Lines</th>
        <td>4</td>
        <td>5</td>
        <td>6</td>
    </tr>
    <tr>
        <th>Purple Line</th>
        <td>7</td>
    </tr>
    <tr>
        <th>Blue Lines</th>
        <td>A</td>
        <td>E</td>
    </tr>
    <tr>
        <th>Orange Lines</th>
        <td>D</td>
        <td>F</td>
        <td>M</td>
    </tr>
    <tr>
        <th>L.Green Line</th>
        <td>G</td>
    </tr>
     <tr>
        <th>Brown Line</th>
        <td>J</td>
    </tr>
     <tr>
        <th>Grey Lines</th>
        <td>L</td>
        <td>S</td>
    </tr>
    <tr>
        <th>Yellow Lines</th>
        <td>N</td>
        <td>Q</td>
        <td>R</td>
    </tr>
</table>
</div>

<h2>Stations-Decision-Points</h2>
<i>The 79 juntions where the challenger must make a decision.</i> <br> </br>
For every decision station on a line, the Station ID, Station Name, Borough, and Line were documented. Additionally, each station on a line was given a "node-number" (there are stations that have multiple node numbers). For example, look at South Ferry Station (<i>Red Line - Bottom Middle</i>) and Canal St on the Blue Line (<i>Middle-Left</i>). South Ferry is the first stop on the 1 line and Canal St is the 10th station on the A line as well as the 9th station on the E line. Their values in the CSV were:
    <table align='center'>
        <tr>
            <th>stationID</th>
            <th>stopName</th>
            <th>borough</th>
            <th>lines</th>
            <th>nodes</th>
        </tr>
        <tr>
            <td>330</td>
            <td>South Ferry</td>
            <td>Manhattan</td>
            <td>X1</td>
            <td>1001</td>
        </tr>
        <tr>
            <td>169</td>
            <td>Canal St</td>
            <td>Manhattan</td>
            <td>A:E</td>
            <td>A010:E009</td>
        </tr>
    </table>
The A and E train stop at Canal St, so both the "lines" and "nodes" column have more than one value, separated by a colon. The colon was used as a separator so that the values could be read independently when loaded into Neo4j (<code>Load-Neo4j-Cypher-Query.sql</code>). Looking at the more complex station, W 4 St-Wash Sq (<i>Blue/Orange Line - Upper Left</i>) where four trains stop at this station: A, D, E, and F train. As before, in the "lines" column and the "nodes" column, every train and their node number were documented:
    <table align:'center'>
        <tr>
            <th>stationID</th>
            <th>stopName</th>
            <th>borough</th>
            <th>lines</th>
            <th>nodes</th>
        </tr>
        <tr>
            <td>167</td>
            <td>W 4 St-Wash Sq</td>
            <td>Manhattan</td>
            <td>A:D:E:F</td>
            <td>A011:D005:E008:F008</td>
        </tr>
    </table>
On the blue line Canal St was A010 and W 4 St-Wash Sq was A011, but what happened to Spring St. Spring St isn't a decision station because if you were traveling from Canal to W 4-St you wouldn't have a choice but to stop at Spring St. <br> </br>

<b>Stations-Official-472</b> <br />
The list of all 472 stations needed to complete the challenge. For example Broadway Junction, although a single point on the map is considered three different stations. One for the A/C, the L, and J/Z trains. 

<b>Stations-Raw</b><br />
The raw station data provided by the MTA website.



<h2>Paths-Decision-Points</h2>
<i>The complete edgelist of the Late-Night Service MTA Subway System</i>. <br> </br>
Modeling the edges was similar to modeling the stations. When modeling stations, each row is a single station and the properties of that station. When modeling edges, each row is a single edge and the properties of that edge. Edges are defined by the two nodes it is connected to, so the first thing needed are the Start Station ID and the Stop Station ID. The three other properties were the routes (same idea as the "lines" column), the nodes (the node numbers), and the distance. In this case, the distance was the <b>time</b> it takes to traverse the edge, or in other words, the time to go from one station to the next. The edge that connects Canal St to W 4 St-Wash Sq is shown below:
 <table align='center'>
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
Although you can traverse this edge on either the A or E train, it is important that this edge is <b>not</b> duplicated in the edge list. If the edge is duplicated, then the program will read it as two separate edges and will solve the problem under the impression that it must traverse the edge twice. After removing all the duplicates there were 104 edges modeled. <br> </br>


<b>Paths-Decision-Points-Subset</b><br />
A simplified subset of the edgelist. The lines modeled are the A,E,J,L trains. <br />

<b>Paths-Matching-Test</b><br />
A super simple edgelist that can be used for testing the program and deciphering what is happening. This edgelist was used in the report to explain the program.



