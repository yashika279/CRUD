function parseDataa(createGraph){
    Papa.parse("cdgi.csv",{
        download: true,
        complete: function(results){
            console.log(results.data);
            createGraph(results.data);
        }
    });
}
function createGraph(data){
    var chart = c3.generate({
        data: {
            columns: [
                [
                    'data1',30,200,100,150,250,50,10]
                ]
            
        },
        axis:{
            x:{
                type:'category',
                categories:['cat1','cat2','cat3','cat4','cat5','cat6','cat7']
            }
        }
    });
}
//parseData(createGraph)