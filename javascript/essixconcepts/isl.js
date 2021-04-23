var isl_2020=[{team:"mcfc",match_played:16,won:10,drawn:4,loss:2,goal_for:25,goal_aqu:11,goal_diff:14,points:34},
             {team:"atkmfc",match_played:16,won:9,drawn:5,loss:2,goal_for:28,goal_aqu:10,goal_diff:18,points:32},
             {team:"gfc",match_played:16,won:8,drawn:4,loss:4,goal_for:20,goal_aqu:11,goal_diff:9,points:28},
             {team:"neufc",match_played:16,won:7,drawn:6,loss:3,goal_for:21,goal_aqu:11,goal_diff:10,points:27},
             {team:"hfc",match_played:16,won:6,drawn:4,loss:6,goal_for:15,goal_aqu:11,goal_diff:4,points:22},
             {team:"ofc",match_played:16,won:5,drawn:5,loss:6,goal_for:18,goal_aqu:10,goal_diff:8,points:20},
             {team:"kbfc",match_played:16,won:4,drawn:4,loss:8,goal_for:10,goal_aqu:11,goal_diff:-1,points:16},
             {team:"bfc",match_played:16,won:3,drawn:6,loss:7,goal_for:11,goal_aqu:11,goal_diff:0,points:15},
            ]


//team name
isl_2020.map(Object=>Object.team).forEach(team=>console.log(team));

//sort the teaams order their matches played
isl_2020.sort((obj1,obj2)=>obj1.match_played>obj2.match_played?-1:1).forEach(obj=>console.log(obj));

//highest points
const mpt=isl_2020.map(obj=>obj.points).reduce((points1,points2)=>points1>points2?points1:points2)
console.log(mpt);

//let data=JSON.parse(isl_2019)
//console.log(data);

//var dataset=[]
//for(let obj of isl_2019){
 //   let object=JSON.parse(obj)
   // dataset.push(object)
//}

//console.log(dataset);