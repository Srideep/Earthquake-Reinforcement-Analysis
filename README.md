# Earthquake-Reinforcement-Analysis
Geospatial Analysis of Japan's Earthquake Reinforcement

# Introduction

This project is used as an urban safety planning template in order to analyze and locate areas of Japan that need extra earthquake reinforcement which are prone to earthquakes and have high population density.

<center>
<img src="https://i.imgur.com/Kuh9gPj.png" width="450"><br/>
</center>

# Earthquakes & Global Plate Boundaries
## Plate Boundaries Dataset
Table for showing top 10 items of the plane boundries dataset

| HAZ_PLATES 	| HAZ_PLAT_1                                        	| HAZ_PLAT_2 	| Shape_Leng 	| coordinates                                       	|
|------------	|---------------------------------------------------	|------------	|------------	|---------------------------------------------------	|
| TRENCH     	| SERAM TROUGH (ACTIVE)                             	| 6722       	| 5.843467   	| [(-5.444200361999947, 133.6808931800001), (-5.... 	|
| TRENCH     	| WETAR THRUST                                      	| 6722       	| 1.829013   	| [(-7.760600482999962, 125.47879802900002), (-7... 	|
| TRENCH     	| TRENCH WEST OF LUZON (MANILA TRENCH) NORTHERN ... 	| 6621       	| 6.743604   	| [(19.817899819000047, 120.09999798800004), (19... 	|
| TRENCH     	| BONIN TRENCH                                      	| 9821       	| 8.329381   	| [(26.175899215000072, 143.20620700100005), (26... 	|
| TRENCH     	| NEW GUINEA TRENCH                                 	| 8001       	| 11.998145  	| [(0.41880004000006466, 132.8273013480001), (0.... 	|
| TRENCH     	| MANOKWARI TROUGH, SOUTH OF NEW GUINEA TRENCH      	| 8001       	| 4.793769   	| [(0.011499698000022818, 131.3704988940001), (-... 	|
| TRENCH     	| MARIANA TRENCH                                    	| 6621       	| 1.311175   	| [(10.99269965800005, 138.9326936230001), (10.9... 	|
| TRENCH     	| MARIANA TRENCH                                    	| 6621       	| 1.411513   	| [(10.981199960000026, 140.2427066990001), (11.... 	|
| TRENCH     	| MARIANA TRENCH                                    	| 6621       	| 20.547210  	| [(11.08020016100005, 141.6506960370001), (11.2... 	|
| TRENCH     	| TRENCH, SOUTH OF SICILY                           	| 3401       	| 1.632744   	| [(37.47190102600007, 13.071900020000044), (37.... 	|

## Historical Earthquake
Table for showing top 10 items of the earthquake dataset
| DateTime                | Latitude | Longitude | Depth | Magnitude | MagType | NbStations | Gap | Distance | RMS | Source | EventID      |
|-------------------------|----------|-----------|-------|-----------|---------|------------|-----|----------|-----|--------|--------------|
| 1970-01-04 17:00:40.200 | 24.139   | 102.503   | 31.0  | 7.5       | Ms      | 90.0       | NaN | NaN      | 0.0 | NEI    | 1.970010e+09 |
| 1970-01-06 05:35:51.800 | -9.628   | 151.458   | 8.0   | 6.2       | Ms      | 85.0       | NaN | NaN      | 0.0 | NEI    | 1.970011e+09 |
| 1970-01-08 17:12:39.100 | -34.741  | 178.568   | 179.0 | 6.1       | Mb      | 59.0       | NaN | NaN      | 0.0 | NEI    | 1.970011e+09 |
| 1970-01-10 12:07:08.600 | 6.825    | 126.737   | 73.0  | 6.1       | Mb      | 91.0       | NaN | NaN      | 0.0 | NEI    | 1.970011e+09 |
| 1970-01-16 08:05:39.000 | 60.280   | -152.660  | 85.0  | 6.0       | ML      | 0.0        | NaN | NaN      | NaN | AK     | NaN          |
| 1970-01-20 07:19:51.200 | -25.800  | -177.349  | 80.0  | 6.5       | Mb      | 175.0      | NaN | NaN      | 0.0 | NEI    | 1.970012e+09 |
| 1970-01-20 17:33:05.400 | 42.519   | 142.966   | 46.0  | 6.4       | Ms      | 199.0      | NaN | NaN      | 0.0 | NEI    | 1.970012e+09 |
| 1970-01-21 17:51:38.500 | 7.017    | -104.298  | 33.0  | 6.6       | Ms      | 140.0      | NaN | NaN      | 0.0 | NEI    | 1.970012e+09 |
| 1970-01-26 10:01:20.500 | -12.579  | 166.370   | 50.0  | 6.4       | Ms      | 91.0       | NaN | NaN      | 0.0 | NEI    | 1.970013e+09 |
| 1970-02-04 05:08:48.000 | 15.532   | -99.484   | 21.0  | 6.5       | Ms      | 100.0      | NaN | NaN      | 0.0 | NEI    | 1.970020e+09 |

## Plate Boundries Visualization
<center>
<img src="q_1.html" width="450"><br/>
</center>
