<img align='right' width='300' style="float:right;" src="./Images/0000.Subway-Time.png" />

<div align='center'>
    <b> Data Science = Solving Problems = Happiness </b>
</div>
<div align='center'>
    <h1> The Subway Challenge</h1>
</div>
<div align='center'>
    Denzel S. Williams
</div>
<div align='center'>
    <i>Springboard Data Science Track '21</i>
</div>
<div align='center'>
    <a href="https://linkedin.com/in/williamdst">
        <img align='center' src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width="75" />
    </a>
    <a href="https://nbviewer.jupyter.org/github/Williamdst/The-Subway-Challenge/blob/main/Subway-Report.ipynb">
        <img align='center' src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white" width='84'/>
    </a> 
    <a href="https://github.com/Williamdst/The-Subway-Challenge/blob/main/Subway-Presentation.pdf" />
        <img align='center' src="https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white" width='150' />
    </a>
</div> 

<h2>0. Inspiration </h2>
I'm sort of an efficiency junkie and I have always enjoyed logistics, optimization, and basically anything that involves how people/things move. I honestly have no clue how I came across the <a href="https://en.wikipedia.org/wiki/Subway_Challenge">Subway Challenge</a>, but I it is as a massive logistics problem and I COULDN'T RESIST tackling it. <b>Also I want to win a world record.</b>

<h2>I. Introduction </h2>
To set a record in the Subway Challenge a participant must navigate the entire New York City Subway system (network) in the shortest time possible. The challenge requires competitors to stop at all 472 stations in the network and no person currently holds that record <a href="https://en.wikipedia.org/wiki/Subway_Challenge#Guinness_Record_times"> [1] </a>. The most recent record of 21H:28M:14S was set on July 22, 2016 by Matthew Ahn for the 469-Station Challenge <a href="https://www.timeout.com/newyork/blog/solo-straphanger-sets-new-all-station-subway-world-record-090616"> [2]</a>. Aside from beginning at Far Rockaway-Mott Avenue and ending at Flushing-Main Street, the route and methodology he used to beat the record is unknown. <br></br>

<p style='text-align:center', align='center'> <b>The goal of this project is to use graph theory to determine a set of paths that could potentially be used to beat the current record.</b> </p>

<h2>II. Understanding the Problem </h2>
To solve this problem a graph representation of the subway system needs to be constructed. The system can be modeled as a weighted undirected graph, where the weights on the edges are the time it takes to get from one station to the next. Since you can travel in both directions on each line the direction is not needed (<i>there is one station that is an exception</i>). The actual map of the system needs to be translated into nodes and edges; to simplify this translation the <a href="https://new.mta.info/map/5336">Late-Night Subway Service</a> map is used. In the late-night subway map all stations are served though not all lines run; most lines run local, making all stops. The late-night map is a starting point to attempt beating the challenge. The map cannot be used, as is, to beat the challenge because the map is only valid from 00:00 - 06:00 every day. The results of the late-night map will tell you <b>what</b> to do, but not <b>how</b> to do it. <br></br>

Once 06:00 hits, all trains are activated, and express routes are implemented. For example, the late-night A-Train might go to certain stops, but it skips over them in the day. In the day, the A-Train is an express train and staying on it for the entire line wouldn’t take you to every stop. At some point you would have to get off and make a transfer to the local C-train to check off the stops that the A-Train skips. This is the main reason why the objective is to determine a set of paths and not just a single path. The only weight the program understands is the time between stations, it doesn't understand that train switching is expensive. Every time you get off a train you must wait for the next one to arrive, which adds to the overall time. Therefore, the program can only return a set of potential options that a human would then need to filter through.

<h2> III. Modifying a Prepackaged Solution </h2>
In 2017, <a href="https://github.com/brooksandrew">Andrew Brooks</a> was tackling a similar problem which he solved using the NetworkX 2.0 library <a href="https://www.datacamp.com/community/tutorials/networkx-python-graph-tutorial"> [3]</a>. Thankfully, he packaged his solution into the <a href="https://github.com/brooksandrew/postman_problems">postman_problems</a>. With this package, you can plug in your own network and solve the <a href="https://www-m9.ma.tum.de/graph-algorithms/directed-chinese-postman/index_en.html#:~:text=The%20(Chinese)%20Postman%20Problem%2C,then%20return%20to%20the%20origin.">Chinese Postman Problem</a> (CPP). Unfortunately, the Subway Challenge isn't a typical CPP problem. The postman always wants to return to his vehicle, so the CPP finds a path that ends where it began. The Subway Challenge has no such requirement, the sole condition is to travel to all the edges at least once. Andrew's postman_package solves the CPP as is, therefore plugging in the subway network wouldn't work because it would always output a sub-optimal solution. However, with a little bit of network theory, the NetworkX 2.5 update, and some tweaks to his package, I was able to build on his work to solve the problem.
