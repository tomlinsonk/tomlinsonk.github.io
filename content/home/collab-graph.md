+++
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 10  # Order that this section will appear.

title = "Collaboration Network"
subtitle = "People are red, papers are blue."

+++

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.16.1/vis.css" type="text/css" />
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.16.1/vis-network.min.js"> </script>
<div id = "mynetwork" class="col-12" style="height:500px; border: 1px solid lightgray;"></div>

<script type="text/javascript">

              // initialize global variables.
              var edges;
              var nodes;
              var allNodes;
              var allEdges;
              var nodeColors;
              var originalNodes;
              var network;
              var container;
              var options, data;
              var filter = {
                  item : '',
                  property : '',
                  value : []
              };

              

              

              // This method is responsible for drawing the graph, returns the drawn network
              function drawGraph() {
                  var container = document.getElementById('mynetwork');

                  

                  // parsing and collecting nodes and edges from the python
nodes = new vis.DataSet([{"color": "#f54e42", "font": "20px", "id": "Austin R. Benson", "label": "Austin R. Benson", "shape": "dot", "title": "Austin R. Benson"}, {"color": "#f54e42", "font": "20px", "id": "Arnold L Rosenberg", "label": "Arnold L Rosenberg", "shape": "dot", "title": "Arnold L Rosenberg"}, {"color": "#f54e42", "font": "20px", "id": "Thomas Zeng", "label": "Thomas Zeng", "shape": "dot", "title": "Thomas Zeng"}, {"color": "#f54e42", "font": "20px", "id": "Ben Aoki-Sherwood", "label": "Ben Aoki-Sherwood", "shape": "dot", "title": "Ben Aoki-Sherwood"}, {"color": "#f54e42", "font": "20px", "id": "Tina Liu", "label": "Tina Liu", "shape": "dot", "title": "Tina Liu"}, {"color": "#f54e42", "font": "20px", "id": "Anna Ritz", "label": "Anna Ritz", "shape": "dot", "title": "Anna Ritz"}, {"color": "#f54e42", "font": "20px", "id": "Tanvi Namjoshi", "label": "Tanvi Namjoshi", "shape": "dot", "title": "Tanvi Namjoshi"}, {"color": "#f54e42", "font": "20px", "id": "Longqi Yang", "label": "Longqi Yang", "shape": "dot", "title": "Longqi Yang"}, {"color": "#f54e42", "font": "20px", "id": "Johan Ugander", "label": "Johan Ugander", "shape": "dot", "title": "Johan Ugander"}, {"color": "#f54e42", "font": "20px", "id": "Frank Thomson Leighton", "label": "Frank Thomson Leighton", "shape": "dot", "title": "Frank Thomson Leighton"}, {"color": "#f54e42", "font": "20px", "id": "Fan R. K. Chung", "label": "Fan R. K. Chung", "shape": "dot", "title": "Fan R. K. Chung"}, {"color": "#f54e42", "font": "20px", "id": "Mengting Wan", "label": "Mengting Wan", "shape": "dot", "title": "Mengting Wan"}, {"color": "#f54e42", "font": "20px", "id": "Zach DiNardo", "label": "Zach DiNardo", "shape": "dot", "title": "Zach DiNardo"}, {"color": "#f54e42", "font": "20px", "id": "Jaime Teevan", "label": "Jaime Teevan", "shape": "dot", "title": "Jaime Teevan"}, {"color": "#f54e42", "font": "20px", "id": "Catherine Bregou", "label": "Catherine Bregou", "shape": "dot", "title": "Catherine Bregou"}, {"color": "#f54e42", "font": "20px", "id": "Cao Lu", "label": "Cao Lu", "shape": "dot", "title": "Cao Lu"}, {"color": "#f54e42", "font": "20px", "id": "Jennifer Neville", "label": "Jennifer Neville", "shape": "dot", "title": "Jennifer Neville"}, {"color": "#f54e42", "font": "20px", "id": "Paul Erd\u0151s", "label": "Paul Erd\u0151s", "shape": "dot", "title": "Paul Erd\u0151s"}, {"color": "#f54e42", "font": "20px", "id": "Brent Hecht", "label": "Brent Hecht", "shape": "dot", "title": "Brent Hecht"}, {"color": "#f54e42", "font": "20px", "id": "Bonnie Berger", "label": "Bonnie Berger", "shape": "dot", "title": "Bonnie Berger"}, {"color": "#f54e42", "font": "20px", "id": "David Liben-Nowell", "label": "David Liben-Nowell", "shape": "dot", "title": "David Liben-Nowell"}, {"color": "#f54e42", "font": "20px", "id": "Sandeep N Bhatt", "label": "Sandeep N Bhatt", "shape": "dot", "title": "Sandeep N Bhatt"}, {"color": "#f54e42", "font": "20px", "id": "Layla Oesper", "label": "Layla Oesper", "shape": "dot", "title": "Layla Oesper"}, {"color": "#f54e42", "font": "20px", "id": "Patty Commins", "label": "Patty Commins", "shape": "dot", "title": "Patty Commins"}, {"color": "#f54e42", "font": "20px", "id": "Kiran Tomlinson", "label": "Kiran Tomlinson", "shape": "dot", "title": "Kiran Tomlinson"}, {"color": "#f54e42", "font": "20px", "id": "Jon Kleinberg", "label": "Jon Kleinberg", "shape": "dot", "title": "Jon Kleinberg"}, {"color": "#425af5", "id": "Workplace Recommendation with Temporal Network Objectives", "label": "", "shape": "dot", "title": "Workplace Recommendation with Temporal Network Objectives"}, {"color": "#425af5", "id": "Choice Set Optimization Under Discrete Choice Models of Group Decisions", "label": "", "shape": "dot", "title": "Choice Set Optimization Under Discrete Choice Models of Group Decisions"}, {"color": "#425af5", "id": "Parameter, noise, and tree topology effects in tumor phylogeny inference", "label": "", "shape": "dot", "title": "Parameter, noise, and tree topology effects in tumor phylogeny inference"}, {"color": "#425af5", "id": "Reconstructing a three-dimensional model with arbitrary errors", "label": "", "shape": "dot", "title": "Reconstructing a three-dimensional model with arbitrary errors"}, {"color": "#425af5", "id": "Phase Lengths in the Cyclic Cellular Automaton", "label": "", "shape": "dot", "title": "Phase Lengths in the Cyclic Cellular Automaton"}, {"color": "#425af5", "id": "Choice Set Confounding in Discrete Choice", "label": "", "shape": "dot", "title": "Choice Set Confounding in Discrete Choice"}, {"color": "#425af5", "id": "The Moderating Effect of Instant Runoff Voting", "label": "", "shape": "dot", "title": "The Moderating Effect of Instant Runoff Voting"}, {"color": "#425af5", "id": "Distance measures for tumor evolutionary trees", "label": "", "shape": "dot", "title": "Distance measures for tumor evolutionary trees"}, {"color": "#425af5", "id": "Examining tumor phylogeny inference in noisy sequencing data", "label": "", "shape": "dot", "title": "Examining tumor phylogeny inference in noisy sequencing data"}, {"color": "#425af5", "id": "Universal graphs for bounded-degree trees and planar graphs", "label": "", "shape": "dot", "title": "Universal graphs for bounded-degree trees and planar graphs"}, {"color": "#425af5", "id": "Bounding Consideration Probabilities in Consider-Then-Choose Ranking Models", "label": "", "shape": "dot", "title": "Bounding Consideration Probabilities in Consider-Then-Choose Ranking Models"}, {"color": "#425af5", "id": "Summarizing Diverging String Sequences, with Applications to Chain-Letter Petitions", "label": "", "shape": "dot", "title": "Summarizing Diverging String Sequences, with Applications to Chain-Letter Petitions"}, {"color": "#425af5", "id": "On unavoidable graphs", "label": "", "shape": "dot", "title": "On unavoidable graphs"}, {"color": "#425af5", "id": "Learning Interpretable Feature Context Effects in Discrete Choice", "label": "", "shape": "dot", "title": "Learning Interpretable Feature Context Effects in Discrete Choice"}, {"color": "#425af5", "id": "Replicating Electoral Success", "label": "", "shape": "dot", "title": "Replicating Electoral Success"}, {"color": "#425af5", "id": "Targeted Training for Multi-Organization Recommendation", "label": "", "shape": "dot", "title": "Targeted Training for Multi-Organization Recommendation"}, {"color": "#425af5", "id": "Ballot Length in Instant Runoff Voting", "label": "", "shape": "dot", "title": "Ballot Length in Instant Runoff Voting"}, {"color": "#425af5", "id": "Graph-based Methods for Discrete Choice", "label": "", "shape": "dot", "title": "Graph-based Methods for Discrete Choice"}]);
                  edges = new vis.DataSet([{"from": "Examining tumor phylogeny inference in noisy sequencing data", "to": "Kiran Tomlinson"}, {"from": "Examining tumor phylogeny inference in noisy sequencing data", "to": "Layla Oesper"}, {"from": "The Moderating Effect of Instant Runoff Voting", "to": "Kiran Tomlinson"}, {"from": "The Moderating Effect of Instant Runoff Voting", "to": "Johan Ugander"}, {"from": "The Moderating Effect of Instant Runoff Voting", "to": "Jon Kleinberg"}, {"from": "Graph-based Methods for Discrete Choice", "to": "Kiran Tomlinson"}, {"from": "Graph-based Methods for Discrete Choice", "to": "Austin R. Benson"}, {"from": "Ballot Length in Instant Runoff Voting", "to": "Kiran Tomlinson"}, {"from": "Ballot Length in Instant Runoff Voting", "to": "Johan Ugander"}, {"from": "Ballot Length in Instant Runoff Voting", "to": "Jon Kleinberg"}, {"from": "Targeted Training for Multi-Organization Recommendation", "to": "Kiran Tomlinson"}, {"from": "Targeted Training for Multi-Organization Recommendation", "to": "Mengting Wan"}, {"from": "Targeted Training for Multi-Organization Recommendation", "to": "Cao Lu"}, {"from": "Targeted Training for Multi-Organization Recommendation", "to": "Brent Hecht"}, {"from": "Targeted Training for Multi-Organization Recommendation", "to": "Jaime Teevan"}, {"from": "Targeted Training for Multi-Organization Recommendation", "to": "Longqi Yang"}, {"from": "Workplace Recommendation with Temporal Network Objectives", "to": "Kiran Tomlinson"}, {"from": "Workplace Recommendation with Temporal Network Objectives", "to": "Jennifer Neville"}, {"from": "Workplace Recommendation with Temporal Network Objectives", "to": "Longqi Yang"}, {"from": "Workplace Recommendation with Temporal Network Objectives", "to": "Mengting Wan"}, {"from": "Workplace Recommendation with Temporal Network Objectives", "to": "Cao Lu"}, {"from": "Phase Lengths in the Cyclic Cellular Automaton", "to": "Kiran Tomlinson"}, {"from": "Parameter, noise, and tree topology effects in tumor phylogeny inference", "to": "Kiran Tomlinson"}, {"from": "Parameter, noise, and tree topology effects in tumor phylogeny inference", "to": "Layla Oesper"}, {"from": "Summarizing Diverging String Sequences, with Applications to Chain-Letter Petitions", "to": "Patty Commins"}, {"from": "Summarizing Diverging String Sequences, with Applications to Chain-Letter Petitions", "to": "David Liben-Nowell"}, {"from": "Summarizing Diverging String Sequences, with Applications to Chain-Letter Petitions", "to": "Tina Liu"}, {"from": "Summarizing Diverging String Sequences, with Applications to Chain-Letter Petitions", "to": "Kiran Tomlinson"}, {"from": "Distance measures for tumor evolutionary trees", "to": "Zach DiNardo"}, {"from": "Distance measures for tumor evolutionary trees", "to": "Kiran Tomlinson"}, {"from": "Distance measures for tumor evolutionary trees", "to": "Anna Ritz"}, {"from": "Distance measures for tumor evolutionary trees", "to": "Layla Oesper"}, {"from": "Learning Interpretable Feature Context Effects in Discrete Choice", "to": "Kiran Tomlinson"}, {"from": "Learning Interpretable Feature Context Effects in Discrete Choice", "to": "Austin R. Benson"}, {"from": "Choice Set Confounding in Discrete Choice", "to": "Kiran Tomlinson"}, {"from": "Choice Set Confounding in Discrete Choice", "to": "Johan Ugander"}, {"from": "Choice Set Confounding in Discrete Choice", "to": "Austin R. Benson"}, {"from": "Choice Set Optimization Under Discrete Choice Models of Group Decisions", "to": "Kiran Tomlinson"}, {"from": "Choice Set Optimization Under Discrete Choice Models of Group Decisions", "to": "Austin R. Benson"}, {"from": "Reconstructing a three-dimensional model with arbitrary errors", "to": "Bonnie Berger"}, {"from": "Reconstructing a three-dimensional model with arbitrary errors", "to": "Jon Kleinberg"}, {"from": "Reconstructing a three-dimensional model with arbitrary errors", "to": "Frank Thomson Leighton"}, {"from": "Universal graphs for bounded-degree trees and planar graphs", "to": "Sandeep N Bhatt"}, {"from": "Universal graphs for bounded-degree trees and planar graphs", "to": "Fan R. K. Chung"}, {"from": "Universal graphs for bounded-degree trees and planar graphs", "to": "Frank Thomson Leighton"}, {"from": "Universal graphs for bounded-degree trees and planar graphs", "to": "Arnold L Rosenberg"}, {"from": "On unavoidable graphs", "to": "Fan R. K. Chung"}, {"from": "On unavoidable graphs", "to": "Paul Erd\u0151s"}, {"from": "Bounding Consideration Probabilities in Consider-Then-Choose Ranking Models", "to": "Ben Aoki-Sherwood"}, {"from": "Bounding Consideration Probabilities in Consider-Then-Choose Ranking Models", "to": "Catherine Bregou"}, {"from": "Bounding Consideration Probabilities in Consider-Then-Choose Ranking Models", "to": "David Liben-Nowell"}, {"from": "Bounding Consideration Probabilities in Consider-Then-Choose Ranking Models", "to": "Kiran Tomlinson"}, {"from": "Bounding Consideration Probabilities in Consider-Then-Choose Ranking Models", "to": "Thomas Zeng"}, {"from": "Replicating Electoral Success", "to": "Kiran Tomlinson"}, {"from": "Replicating Electoral Success", "to": "Tanvi Namjoshi"}, {"from": "Replicating Electoral Success", "to": "Johan Ugander"}, {"from": "Replicating Electoral Success", "to": "Jon Kleinberg"}]);

                  nodeColors = {};
                  allNodes = nodes.get({ returnType: "Object" });
                  for (nodeId in allNodes) {
                    nodeColors[nodeId] = allNodes[nodeId].color;
                  }
                  allEdges = edges.get({ returnType: "Object" });
                  // adding nodes and edges to the graph
                  data = {nodes: nodes, edges: edges};

                  var options = {
    "configure": {
        "enabled": false
    },
    "edges": {
        "color": {
            "inherit": true
        },
        "smooth": {
            "enabled": true,
            "type": "dynamic"
        }
    },
    "interaction": {
        "dragNodes": true,
        "hideEdgesOnDrag": false,
        "hideNodesOnDrag": false
    },
    "physics": {
        "enabled": true,
        "stabilization": {
            "enabled": true,
            "fit": true,
            "iterations": 1000,
            "onlyDynamicEdges": false,
            "updateInterval": 50
        }
    }
};

                  


                  

                  network = new vis.Network(container, data, options);

                  

                  

                  


                  

                  return network;

              }
              drawGraph();
</script>   