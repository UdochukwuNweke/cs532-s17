var nodes, links;
var link, node;

var width = window.innerWidth - 10;
var height = window.innerHeight - 50;
var radius = 6;

var force = d3.layout.force()
        .linkDistance(150)
        .charge(-120)
        .gravity(.05)
        .size([width, height])
        .on("tick", tick);
var tip;
d3.json("data/followers.json", function(data) 
{
    // http://blog.thomsonreuters.com/index.php/mobile-patent-suits-graphic-of-the-day/
    links = data;

    var svg = d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height);


    tip = d3.tip()
        .attr('class', 'd3-tip')
        .offset([-10, 0])
        .html(function(d) 
        {
            var tooltip = '<span>' + d.name + '</span><br>';

            if( d.picture )
            {
                tooltip += '<img height="100" width="100" src="'+d.picture+'"><img>';    
            }

            return tooltip;
        });

    svg.call(tip);

    svg.append('defs').append('marker')
            .attr({'id':'arrowhead',
            'viewBox':'-0 -5 10 10',
            'refX':25,//position of arrow on line
            'refY':0,
            //'markerUnits':'strokeWidth',
            'orient':'auto',
            'markerWidth':4,//size of arrowhead
            'markerHeight':4,//size of arrowhead
            'xoverflow':'visible'})
            .append('svg:path')
                .attr('d', 'M 0,-5 L 10 ,0 L 0,5')
                .attr('fill', '#ccc')
                .attr('stroke','#ccc');

    link = svg.selectAll(".link");
    node = svg.selectAll(".node");

    //credit for edge labels: http://bl.ocks.org/jhb/5955887
    //credit for main vis: http://bl.ocks.org/mbostock/2706022

    nodes = {};
    // Compute the distinct nodes from the links.
    links.forEach(function(link)
    {
        link.source = nodes[link.source] || (nodes[link.source] = {name: link.source});
        link.target = nodes[link.target] || (nodes[link.target] = {name: link.target});
    });

    update();
});

function update()
{
    console.log('\nupdate():');
    console.log('\tnodes:', nodes);

    // Restart the force layout.
    force
        .nodes(d3.values(nodes))
        .links(links)
        .start();

    // Update links.
    link = link.data(force.links());
    link.exit().remove();
    link.enter().append("line")
        .attr("class", "link")
        //.attr("id",function(d,i) {return 'edge'+i})
        .attr('marker-end','url(#arrowhead)')
        .style("stroke","blue")
        .style("stroke-opacity", 0.2);

    // Update nodes.
    node = node.data(force.nodes());
    node.exit().remove();

    
    var nodeEnter = node.enter().append("g")
        .attr("class", "node")
        .on("mouseover", tip.show)
        .on("mouseout", tip.hide)
        .on("click", function(d)
        {

            if(d3.event.defaultPrevented)
            {
                console.log('\tdrag:', d);
                return; // ignore drag
            }
            
        })
        .call(force.drag);
    
    nodeEnter.append("circle")
    .attr("r", radius - .75);

    nodeEnter.append("text")
        .attr("x", 12)
        .attr("dy", ".35em");

    node.select("circle")
        .style("fill", 'red')
        .style("fill-opacity", 0.8);

}

function tick()
{
    node
        .attr("transform", function(d)
        {
            d.x = Math.max(radius, Math.min(width - radius, d.x));
            d.y = Math.max(radius, Math.min(height - radius, d.y));
            return "translate(" + d.x + "," + d.y + ")";
        });
    
    link
        .attr("x1", function(d)
        {
            return d.source.x;
        })
        .attr("y1", function(d)
        {
            return d.source.y;
        })
        .attr("x2", function(d)
        {
            return d.target.x;
        })
        .attr("y2", function(d)
        {
            return d.target.y;
        });
    
    
}

function mouseover()
{
    tip.show();
}

function mouseout()
{
    tip.hide();
}