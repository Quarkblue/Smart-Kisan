farming_style = {'jute': 'classic style farming','pomegranate' : 'square method', 'banana' : 'division of suckers', 'papaya' : 'nursery breeding', 'apple' : 'pit farming', 'mango' : 'side grafting farming', 'lentil' : 'irigation farming', 'pigeonpeas' : 'flat sowing', 'blackgram' : 'irrigation farming', 'coconut' : 'pit farming', 'muskmelon' : 'pit farming', 'kidneybeans' : 'classical farming', 'rice' : 'paddy cultivation farming', 'mothbeans': 'regular farming','mungbean': 'broadcare farming', 'coffee': 'shade growing', 'grapes' : 'viticulture farming', 'watermelon': 'watermelon farming', 'maize' : 'regular farming', 'orange':'regular farming', 'cotton':'regular farming', 'chickpea':'regular farming'}

MESSAGE_MONTH = "Hey Smart Kisan! Here are some tips for you: We recommend you to grow crop_recommendation the next season! Try to use the following organic fertilizers for better results: Vermicompost Fertilizer for all plants. Confirm that you bought it by typing a Yes, and we will send you daily updates of schedules on how to use it alongside your current fertilizers so as to mazimize the yield! We are working towards connecting you to the sellers directly, expect an update soon! Season is round the corner, for better yield, try farming_style farming. For weekly tips, reply with (organic tips). Organic Tip of the Day: random.choice(organic_tip) farming"


NITROGEN = [ 90,  85,  60,  74,  78,  69,  94,  89,  68,  91,  93,  77,  88,
        76,  67,  83,  98,  66,  97,  84,  73,  92,  95e,  99,  63,  62,
        64,  82,  79,  65,  75,  71,  72,  70,  86,  61,  81,  80, 100,
        87,  96,  40,  23,  39,  22,  36,  32,  58,  59,  42,  28,  43,
        27,  50,  25,  31,  26,  54,  57,  49,  46,  38,  35,  52,  44,
        24,  29,  20,  56,  37,  51,  41,  34,  30,  33,  47,  53,  45,
        48,  13,   2,  17,  12,   6,  10,  19,  11,  18,  21,  16,   9,
         1,   7,   8,   0,   3,   4,   5,  14,  15,  55, 105, 108, 118,
       101, 106, 109, 117, 114, 110, 112, 111, 102, 116, 119, 107, 104,
       103, 120, 113, 115, 133, 136, 126, 121, 129, 122, 140, 131, 135, 
       123, 125, 139, 132, 127, 130, 134]
PHOSPHORUS = [ 42,  58,  55,  35,  37,  53,  54,  46,  56,  50,  48,  38,  45,
        40,  59,  41,  47,  49,  51,  57,  39,  43,  44,  60,  52,  36,
        72,  67,  73,  70,  62,  74,  66,  63,  71,  78,  80,  68,  65,
        77,  76,  79,  61,  64,  69,  75,  24,  18,  26,  27,  25,  21,
        30,  11,   5,  10,   7,  20,  22,  15,  23,   8,  16,  29,  17,
         6,  19,  13,   9,  14,  28,  94,  95,  92,  89,  88,  87,  85,
        86,  83,  91,  81,  84,  90,  82,  93,  33,  31,  34,  32, 130,
       144, 123, 125, 131, 140, 122, 134, 145, 139, 141, 138, 136, 132,
       133, 121, 126, 120, 142, 135, 129, 128, 137, 127, 124, 143,  12]
POTASSIUM = [ 43,  41,  44,  40,  42,  38,  36,  37,  39,  35,  45,  16,  17,
        21,  20,  19,  25,  22,  15,  18,  23,  24,  77,  84,  85,  81,
        75,  79,  76,  83,  78,  80,  82,  46,  50,  53,  54,  49,  55,
        52,  47,  48,  51,  27,  31,  32,  34,  33,  30,  28,  29,  26,
       195, 204, 205, 196, 198, 197, 203, 201, 202, 199, 200,  12,  13,
         6,   9,  10,  14,   8,   7,   5,  11]
PH = [6.502985292000001,7.038096361,7.840207144,6.980400905,7.628472891,7.073453503,5.70080568,5.718627177999999,6.685346424,6.336253525,5.386167788,7.50283396,5.108681786,6.98435366,6.94801983,7.042299068999999,6.2490506560000005,6.970859754,5.953933276,5.85393208,6.442475375,5.070175667,6.012632591,6.254028451,7.375482851,7.778915154,6.2865001760000006,7.070959995,6.244841491,6.043304899,5.824709117,6.3573893660000005,6.364134967999999,5.01450727,6.149410611,5.950660556,5.960370061,5.561398642,7.416245107000001,5.583370042,6.430010215,5.534878156,6.903985986,6.271478837999999,7.224285503,6.13428721,5.206373153,7.782051312999999,7.062779015,7.730367824,5.286203711000001,6.766240045,7.382762603,5.658169482000001,5.543360237999999,6.215109715,7.120272972,5.950647577000001,7.236705436,6.501697816,7.592490617,5.875345751,6.932400225,6.9462098810000015,5.739175027000001,6.738652179,5.5948196260000005,6.946636369,5.012139669,6.363472207999999,6.880431223,7.300410836,6.587918707999999,7.283736617000001,7.023936392,6.939083505,7.868474653,5.005306977,6.136131869,7.5240800760000015,5.706943251,5.758506323,6.349606327,5.9999690260000005,5.453592032,6.372576327000001,5.105588355,5.9353444060000005,5.17782304,6.462391607000001,7.069172227,7.473134377,6.158376967000001,7.549873681,6.028321557999999,6.604993475,6.500343222000001,5.935745417000001,7.072655622,5.333322606,5.7499144210000015,6.931756557999999,6.657964753,6.596060648,5.970458434,6.158830619,6.047906679,5.913664501,5.855442401,5.750254943,5.852607099,6.4725232870000005,6.9670577620000005,6.082973754,5.919045532,6.204747652999999,6.600827017,6.021902237000001,6.033550195,6.28886807,6.550563822999999,5.573286437,6.829199275,5.716222912,5.54990242,6.586244581,5.893093135,5.918263801,5.588650585,6.576418207000001,6.178056304,6.641906353,6.489040367,5.680361037999999,6.625404347999999,6.524478032,5.696205468,6.803931519,6.252797547999999,6.092725883,6.234330356,5.722579819,6.430616465,5.983952675,6.80163854,6.499936446,6.265564338,6.727303282,6.325235159,6.807487794,6.671085817000001,6.648725327,6.439071996,6.474476516,5.871647806,5.730617109,5.850439831,5.791649933,6.740000687999999,6.272417541,5.715208817000001,5.773454729,5.584171461,5.787268394,5.77597783,6.864793607,6.192360002999999,6.636803222999999,5.826426917,6.960358276,6.11275104,6.708446922,5.561510732,5.873242491,6.995843776,5.714799723,6.78073637,5.513697923,5.798423907999999,6.352471866,6.822586546,6.655426355,6.1212940410000005,5.790770202999999,6.47444292,6.455116637000001,6.6069840860000015,6.330554389,6.5286312660000005,5.721667141,6.644205485,6.376651091,6.247040422,6.656730007999999,6.2048017,6.158860284,6.385684213999999,6.417820493,6.381201909,6.877869005,7.485996067,6.920251378,5.9969320370000005,6.391173589,7.152811172000001,5.988992796000002,6.231049027999999,7.550808267000001,7.010570541,8.753795334,8.718192847000001,7.976607593,6.515499548999999,8.490127142,6.576415562,6.481783042999999,7.966605025,8.140825437,7.228963452,6.492546046,7.528599957000001,7.701446446,8.519975748,6.620900869,8.104396057999999,6.204090835,6.051091339,7.690962337999999,7.8292111439999985,6.761599706,6.654425315,6.129533877,8.829273328,8.621662982,8.204862075,6.18042747,7.978996755,7.863113671,6.967843048,6.206582192999999,8.868741443,8.766128654,8.736337905,8.081095263,6.138243973,7.496645259,8.380185271,6.289614016,6.586777189,6.89655198,7.8067476560000015,7.150681303,6.64919573,7.778591617999999,6.358740355,8.255450758,6.456148474,6.613072145,8.165359297,7.64867466,6.545888558,7.1042247970000005,7.358099622,6.4740245000000005,7.840339388999999,7.064790365,7.599033472,6.715587232000001,6.81712422,7.985417393,7.545258424,7.728998197,7.354973451,7.313122235,7.785039076,6.307004922999999,6.4039823160000005,7.599279991,7.217018459,7.561108006,7.489545074,6.609696734,7.476800943,7.325451279,6.489389282,7.786366322,6.4084378860000015,8.423873703,8.719960893,7.811997977000001,6.317153205,7.114405288,8.135900726000001,7.714153037999999,7.103798069,8.861479668,7.861128148,7.4526709,7.168096055,7.26311855,5.68597166,5.759237003,5.873171894,5.926676985,5.95561668,5.9499490810000015,5.789214288999999,5.581021521,5.689858133,5.794158503999999,5.748190462999999,5.566522896,5.809419584,5.887263027,5.99812453,5.792744849,5.912289889,5.7883869510000014,5.728233081,5.833940084,5.967533236,5.6250964460000015,5.515615023,5.954665349,5.74644777,5.877347515,5.979973965,5.635993966,5.635231778,5.679224346,5.670062975,5.724242065,5.811314232000001,5.783425416,5.607808432000001,5.946999529,5.852046999,5.824090984,5.502999119,5.821649914,5.711439256,5.514927264,5.99616119,5.695422862999999,5.833010957999999,5.568456899,5.645435626,5.821194486,5.659254981,5.945465949,5.9511774520000005,5.520880013999999,5.578410206,5.608165195,5.609435127999999,5.509295379,5.902033406,5.744117663,5.717143397,5.542690119,5.858617867,5.618844277000001,5.6066203460000015,5.582178402,5.56503533,5.889614577000001,5.934136378,5.683548308,5.70836603,5.948164454,5.774755143999999,5.97229163,5.532100554,5.669560726,5.655726817000001,5.591704013999999,5.932323085,5.824208308999999,5.86442953,5.866744372,5.706198621,5.940546818,5.916779289,5.779090476,5.82738029,5.514234138,5.662699104,5.86390397,5.624690247999999,5.591560999,5.976312537999999,5.669236258,5.961934481,5.690065688,5.698371311,5.59503163,5.5259045260000015,5.819403771,5.562201934,5.630664753,6.03160778,5.269084669,5.985792703,6.09186275,5.624731337999999,6.446091759,5.623490042999999,5.864623352000001,5.761702519,4.696518678,5.269504214,7.445444882999999,5.833031707999999,7.3393209289999986,6.347929353,4.697750704,4.962661422,4.964887857,5.642813116,5.6093956,4.681576043,5.70951224,6.413543781,6.007508163,4.946369874,5.517208078,5.902103172,5.719889876,4.548202098,6.6695294160000005,4.7509292180000005,4.946263888,5.266227032,7.10959773,5.617008201,5.632353113,4.674941549,7.161797643,6.624966131,5.004074623999999,6.3458060110000005,6.216814453,5.921666758,6.012719118,4.684079249,7.077170002000001,6.208843215,7.05181629,4.722222454,6.418062652000001,4.803564468,4.608695247,5.611510977000001,7.322097972000001,5.023115055,5.617122801,5.391560417999999,5.906596905,6.574209678,4.807776748999999,4.760038038999999,5.180271502,4.895927306,6.436160044,7.066087261,6.655918077999999,5.982854522999999,5.457871272999999,4.759490199,7.342409555,4.820788186000001,6.242052013,5.001038726,5.560224582999999,4.747352458,7.313517308,5.661826398,4.672437054,6.471862118,5.384762927000001,5.8598134160000015,6.962386495,6.12166671,6.421748487,4.828936119,6.98571967,4.603563116,6.979540061,7.064973419,5.16516459,5.111488821,5.374358869,5.671419084,5.667419697000001,6.07938452,6.931924962999999,6.842744374,6.876572502999999,6.151029296,4.567446499,3.692863601,4.371745575,8.399135957999999,8.840656256,8.153022903,5.270749441,8.050304395,9.679240873,6.974978386,7.39389918,6.68727523,7.88118645,5.875333778,8.202706015,8.985348193,5.87707519,7.707595055,4.524171562,9.926212291,6.455592696,8.016210782,3.71105919,5.49091063,9.254089438,6.005242945,7.437078236,3.808429173,5.818219385,4.52363558,3.510404312,6.030447288,5.498340807999999,4.61136408,5.545219232000001,8.292875733999999,3.828031463,8.869532817,3.793575185,4.193189124,7.661537347999999,9.392694614,4.516154055,5.794289715,7.354286985,5.993513566,8.620107545,9.45949344,8.0344125,5.414492777,6.2760043360000015,9.160691747,7.887658711,8.183844843,9.072011412,7.702287236,5.88509677,6.16496284,3.504752314,7.388007482999999,8.340398059,8.66077954,3.558822825,5.9565851,9.416003106,8.18422855,5.131779302,6.294130312999999,7.991902443,8.923095695,6.878498176,5.243634848999999,7.550090941,8.709291687999999,7.792508067999999,8.055908857999999,4.397698806,5.9523849570000005,8.532078732999999,7.224193642,4.931890506,4.626212446,5.026003659,3.5253661,8.86979671,9.406887533,5.80428611,8.35495812,8.634929739,7.699200949,5.261285926,9.112771682,4.605700542,7.115994051,7.214078621,9.93509073,8.914074888,8.639586199,8.621514073,5.838508699,3.532008668,7.18530147,7.034214276,6.635968697999999,6.828187498999998,6.89077995,7.165121108999998,6.935804256,7.196774236,6.990095452,7.064782137999999,7.156563094,6.364967184,6.428054409,6.664187809,6.637677489,6.79385576,6.852884642999999,7.121571293,6.883308033,6.421271178,6.54450214,6.452006451,6.489259136,6.713410626,6.510840928,6.2873801170000005,6.86308576,6.78415271,6.769415887999999,6.320768488,6.705008503999999,6.790736339,7.130278657000001,7.012740397000001,7.1556850160000005,6.991242362,6.218923893,7.199495367999999,6.3898821660000005,6.623438282,7.033012777000001,6.32400451,6.397636709,6.401455706,6.904587016,6.478557136,7.063022095,6.981758362000001,6.227134139,6.232836962,7.140437859,6.459252023,6.568795403999999,7.12851089,6.42937879,6.248900919,6.619891497999999,6.377568542000001,6.415459592,6.3206620120000006,6.978400282000001,6.442335592999999,7.184398832,6.402926221,7.085982325,6.698574085,6.594739424,6.647965508,7.120032489,6.91380932,7.073048264,6.5304707,6.684381357,6.581351374,6.86483915,6.487124217000001,6.605733067999999,6.860602782000001,6.41874299,6.365513634,6.5563729660000005,6.760694227999999,6.715276662999999,6.666380512000001,6.626629798,6.702772465,7.011030515,6.890156495,6.821747052,7.183189922,6.27258822,6.679127482,6.689825155,6.583381939,6.725551062,7.069747813999999,6.921993877999999,6.770955317,6.983130466,6.267684328,7.454532137,7.040056094,7.418650668,6.501869314,6.814410927999999,7.581442888,7.741418772,6.573531614,7.543804222999999,6.5408208,7.22405917,7.551364319,6.928898659,7.747775262999999,6.706505915,6.668238556,7.332375138,7.596802025,7.70650895,7.366542647,6.919243702,7.187721817999999,7.0758864720000005,6.74441168,6.726469087999999,6.628264883,7.127064207,7.538631462000001,7.162357641,6.859409487000001,7.397190844,6.880245789,6.581313137,7.296972161,6.97297656,7.241148507,6.92009048,7.504608385,7.152272256,7.137004749,6.8080417220000005,7.393631868,7.69950698,6.602888248999999,6.734447425,6.521217963,7.707332484,6.596719015,7.403623355,7.517097,7.17620823,6.593961761,7.143942758,6.690655045,7.423530351,6.578714842999999,7.497469256,7.775306272000001,7.322555222999999,7.580527339,7.1084501210000015,7.358974541,7.405176138,6.500144962,7.167435834,7.261791753,7.586642101,7.534811832999999,7.251000789,6.513620917999999,7.121254928,7.574561547,7.350869792,7.5131510760000015,7.0256077060000015,6.804253866,7.163043872,7.338929556,6.621323612,6.661870999,7.733149554,7.402891666,6.599147297999999,7.04174124,7.353876754,7.026795358999999,6.814301033,7.42160832,6.8473828910000005,7.191522601,7.01285529,7.368318809,7.26154329,6.52669158,6.872594461,6.874142175,7.76061831,6.781841984,7.326980454,7.453975408,7.604110177000001,7.728832424,7.491217102,6.633864582,7.324863481,6.410441476,7.836719564,6.139215944,6.590571088,7.286049977999999,6.058306161,6.658605362,7.299360767,7.815210661,5.925391795,6.403683619,7.397546271,7.722335992,7.475926645,6.887130053,7.441976825,7.629910252999999,7.336117221,6.75020529,7.52178027,6.347379185,7.135251532000001,7.670178119,7.399749291,7.841496029,6.254216611,6.868881707999999,7.320514721,6.296976913,7.241151936,7.685959305,6.890760124,6.155915975,6.167855382000001,6.861640036,6.978361689,7.043160241,5.94239222,7.239455147,6.516317561,6.233269045,7.505283615,6.950300686,6.958054839,6.54803469,6.461618577,7.065264073,6.765091462000001,5.91645379,6.711341147000001,6.379881442,6.313284267999999,7.393210848,7.504930973,7.198076286,7.007037515,6.677262562,6.74398035,6.547361617999999,6.551577598,6.585020302999999,6.924042372000001,7.437373666,7.142611056000002,7.74672376,6.300479414,6.078724107,6.76660668,7.641024177,6.559681838,7.072923306,7.732194787999999,6.157782589,7.240988401,6.898905799,6.818681086000002,6.261937875,6.493036868,7.042474679,7.692013657,6.250994222999999,6.0521848810000005,7.002216044,7.272427638,5.962001484,7.080506001,6.5937983870000005,7.28805662,7.32710972,6.366355781,7.011121216,6.280725549,7.621494566,7.630424082999999,7.802212437,5.922935513,5.937649577999999,6.804781106,6.424670614,6.7380162210000005,6.4973666770000005,6.327673765,6.36137446,6.9235093710000015,6.630646082999999,5.832525853,6.738993954,5.782435567,6.537042717,6.145104401,6.890784045,7.175344328,5.938528744,5.709380472,6.184400085,6.553509673,5.885638185,6.1438746910000015,6.101198974,6.594037135,6.8598408210000015,6.56893406,6.769855664,7.130837931,5.7403380020000006,5.843005428,6.648687273999999,6.902751061,6.608023872,6.828522375,6.910374919,6.306605528,7.009180374,6.297907578999999,6.728599215,6.965156737999999,5.578095745,7.199504273,5.841367187,6.710143266,5.972714857000001,5.561851831,6.107054807999999,6.988035315,7.13147457,7.086947687,6.749260456,7.16300467,7.013481515,5.648243648999999,6.610251186,7.054313822999999,6.026999326,5.7794274020000005,6.535244251,5.684995235,6.12476108,6.999014379,6.277148771,6.322396027000001,5.956401828,6.591302797000001,7.104094929,6.407872061,6.658402594,6.276038961,6.825256236,6.368560522,7.005410734,6.8973684770000006,6.152906502,5.744361602000001,7.051654924,6.034612928,6.9244907310000015,6.887005997,6.8444019,5.786058032000001,5.627186257000001,5.700088663,5.567805185,6.077886012,6.397995609,5.767372539,7.079973241,5.893332377999999,7.058222596,5.78270695,6.269663962999999,5.892913826,7.116538883,6.430163481,7.159520979,6.431265737,6.082571701,6.149934034,5.849076099,6.276800323,5.926824754,5.519088423,6.079178787999999,6.13465588,5.808497603999999,5.891458107,5.816622478999999,5.8431631610000005,6.376756632999999,5.623615687000001,5.91505509,6.458714879,5.565028635,6.211833161,6.490074429,5.590236025,6.225225238999999,6.190757458999999,5.915568968,6.195152442,6.156373499,6.313197204,6.324270089,5.7074889870000005,6.119216009,5.571401169,5.63127166,6.101241579,6.438137278999998,6.098369122,5.695267822000001,5.6180944460000015,6.435785799,6.176644228,6.220643671,5.8717022110000014,6.390741836,6.21084479,6.012696655,5.908770059,6.049801781,6.010095852999999,5.738678895,5.74055541,5.793260262,5.50947065,5.986442306,5.790768046,5.915546415,6.242528277999999,6.0360792660000016,5.829898502000001,6.088064451,6.469370954,5.720726906,5.80766417,5.703381727999999,6.165001277999999,6.002481605,6.212369363,5.765308943,5.740764682000001,5.879119455,6.099478745,5.674403358999999,5.694243847,5.905494703,6.110844721,6.020445317,6.435917308,5.505393832999999,5.677719902000001,5.719014989,6.275572297999999,6.275384607,6.201911642000001,5.758054257,6.3239336470000005,5.901100841,5.644486582000001,6.235461772000001,6.28236237,6.356090905,5.837258235,5.653437902,5.727469947,6.200111067999999,5.614471478,6.257369799,6.037430836,5.760457558,6.1581644220000005,6.387431382999999,5.891413895,5.725418961,6.281069505,5.507641777999999,5.954626604,4.757114897,5.6995869720000005,5.977413802999999,6.430139436,6.113935087000001,5.074272692,5.667507706,5.978634285,5.064613314,4.772385986000001,5.161148592,6.797779227,6.39474303,5.566704378,5.755049971,5.417340525,6.166173833999999,5.191265116,4.954739564,5.664587011,5.548584852,6.804437106,6.097869767000001,5.075504537,4.546466109,5.855119267999999,6.442393461,4.507523551,6.10729559,6.47544932,6.832979508999999,5.395275719,6.13526938,4.555688532,6.4341977560000005,5.316875978000001,5.279388967,6.720041791,5.72742254,4.691396195,6.810186079,6.454045329,5.842763773,5.024124683999999,6.422710539,4.94295037,6.414526606,6.777788126,6.441328044,4.650536197,5.254532213,5.910634533,4.755273631000001,6.814630246,5.342866119,6.336234623999999,4.754435025,6.831706773,6.9674177660000005,4.947683034,5.630619901,6.27339822,6.472774648,6.953246506,5.6437102160000014,6.392313972999999,4.981816523,5.421265282999999,6.942520105,5.435840509,5.870116071,4.74910393,5.497946899,6.811291098,6.460542749,4.791146778,6.4841522000000005,6.526654345,6.279133738,6.052026047000001,5.73171945,5.32307197,4.66910839,5.101206389,5.339556562,5.061081874,5.8211060360000015,5.956027059,5.676032581,6.524114355,6.2739536760000005,6.128167757000001,4.934964765,5.445008416,4.525722333,5.403908327999999,6.621623545,6.207495815,5.418475257000001,6.112305667,6.092241627000001,5.896343436,6.15526103,5.732453638,6.253034534,6.106190557000001,5.647202395,6.130310493,6.499604931,5.554831977,5.800242694,5.570290539,6.27564088,5.536645599,6.208196881,5.870600622,6.334771461,5.856575335,5.898944282,5.775600435,5.931101816,6.2286454,5.594240602999999,5.569230319,5.93202852,6.423216506,6.417500829,6.234904253,6.000573725,5.6851027689999984,5.662140095,6.358186848,6.119495295,6.207600782999999,6.48754639,5.81717753,6.325480034,5.562790949,6.487369687,6.116982944,5.695792761,5.7343170070000005,6.329499832000001,6.167013532,5.653776057999999,5.840256272,5.5399808120000005,5.833302165,6.399433771,6.138958698,5.972850837999999,6.456079585,6.3364266670000005,6.425419926,6.2943956760000015,6.477768039,5.931538447,5.980598579,6.389783283,5.693287415,6.00299607,6.372959542,5.510924848999999,5.69945282,5.778594403,6.315586313,5.9718130060000005,5.891195653,6.129812716,6.313085601,6.053662544,5.804799142,6.400719746,5.953966361,5.6092559920000005,5.777271492000001,5.682395429,5.863996687,6.444373116,5.550832177999999,6.107741787999999,5.620745638,6.349875906,6.484323189,5.838748311,6.29099842,5.638328481,6.415555956,6.323722572,5.757009965,6.1586894060000015,5.7335398070000005,5.908724337000001,6.361141107000001,5.96537863,6.476757723,6.224542938,6.209928251,5.841138354,6.283818329,6.818261382999999,6.37620108,6.581587932000001,6.932739726,6.140099215,6.467095849,6.849471704,6.512196212,6.039584629,6.057697106,6.423898762,6.936997681,6.251286661,6.190015912000001,6.681606702000001,6.51075991,6.770278088,6.429788072999999,6.209888345,6.419052193,6.237861736,6.762471628999998,6.612847999,6.704688865,6.049609892,6.762030215,6.65398725,6.738030547,6.095689937,6.538006356,6.377427122,6.417011754,6.649086972,6.25933595,6.121168559,6.031424482,6.835268183999999,6.5517503060000015,6.940236218,6.87606733,6.457216535,6.921847887999999,6.8814257460000015,6.915717008,6.206247493999999,6.29542477,6.399669044,6.862157042000001,6.224066378,6.093814669,6.291540277999999,6.32281728,6.873283991,6.074209622000001,6.49889585,6.678805092,6.114128685,6.405054243,6.110142735,6.828982708,6.451499763999999,6.313512998999999,6.755192025,6.623167177000001,6.12532356,6.653867608,6.343942518,6.217300786,6.286387658,6.769893799999998,6.744966312000001,6.391858432,6.770434148,6.727468157000001,6.662244646,6.944640222,6.507110986,6.520663422,6.106500787000001,6.277484042999999,6.195142279,6.792035575,6.472756256,6.000975617000001,6.5877912620000005,6.956508826,6.259086582999999,6.747537642,6.932537231,6.353107392999999,6.211748957,6.277245253999999,6.560443519,6.903020221,6.765094963999998,6.189213927000001,6.904241707000001,6.463271076,6.260838965,6.776533055,6.528404377999999,6.750145572,6.562832807,6.117530021,6.076459669,6.293486295,6.069171847000001,6.740983646,6.201797639,6.041027474,6.019372459,6.704104127000001,6.494251024,6.224535448999998,6.160414414,6.168757984,6.085444691,6.1590508160000015,6.606033244,6.447662945,6.105909623,6.559763394,6.14410903,6.099662369,6.413927319,6.0751441160000015,6.123802502,6.698468621,6.088885814,6.367800632000001,6.425930938,6.469983276000002,6.094016337999999,6.150090898999999,6.646962425,6.379690748,6.732834334,6.126019932,6.161123579,6.442810053,6.732049075,6.243673725,6.266208727,6.350623739,6.002927293,6.342573112,6.163921247999999,6.121745389,6.130160472999999,6.440584681,6.185053234,6.157724816,6.776987974,6.431970877,6.708743843,6.010739645,6.365956657999999,6.6683827660000015,6.74669542,6.031665834,6.40077205,6.448792688999999,6.251420275,6.2744528110000015,6.135996372,6.194090172,6.327822962000001,6.2125672110000005,6.640470862999999,6.685553129,6.327210469,6.35544263,6.085682343999999,6.781050372999999,6.630301421,6.484799661,6.566759102000001,6.170520517999999,6.0124803510000016,6.541150335,6.341400922,6.150686363999999,6.438008152999999,6.547041902999999,6.399891457000001,6.186770318,6.159020864,6.660954816,6.504906978999999,6.706053225,6.067665497999999,6.419083092,6.39637861,6.375923383,6.700337732,6.565312652999999,6.286515359,6.448061578,6.585872508,5.521466996,6.133220586,6.226289556,6.321152192,5.587905967,5.824151692999999,5.7721799460000005,5.790993052,6.4992268210000015,5.658473817000001,5.573241391,6.079497202000001,6.3831802710000005,5.867420996,5.708418722,5.7983508000000015,6.28188384,5.697945522,5.6059340870000005,5.85648105,6.041053829,5.685062404,5.669489065,5.751707342,5.800448951,5.821347769,6.28022267,6.027314401,5.636687393,5.559363609,5.596449493,5.893492998999999,5.875718516,6.386021424,5.710819862,5.7959857160000015,6.046673619,6.443382913,5.617227184,6.442289294,6.162034371,5.812781806,5.7650151260000015,6.184922574,5.739652177000001,5.8247786360000005,5.554823557000001,6.024248787,5.631333387000001,5.811975094,5.730557448,5.66999105,5.682751473,6.245858905,6.017370134,5.53456749,5.952367662,6.126436584,6.406818518,6.155939452999999,5.878568981,5.935336307999999,5.971332179,5.67130617,5.882155987999999,6.08551916,5.90402645,6.1102188260000005,6.212302608,6.142803397000001,6.365972687999999,6.264202804,6.276198595,5.514253142,5.682343744,5.830892252000001,5.603413172000001,6.0967531,6.056529526,6.160267496,5.814434775,5.987262638,5.570020684,5.9655513110000005,6.062356467000001,5.895319002000001,6.119432215,5.624203283,5.52078314,5.731535257999999,5.893490899,5.560521058,6.222390797999999,6.071255131,6.231950009,5.889480679,5.732757516,6.400321212000001,6.496934492,6.229498836,6.354006743999999,7.511755067999999,7.335158382,7.813916602999999,7.1291369410000005,6.079998496,7.408939392000001,7.207991261,7.189259647,7.365338111,7.455991072000001,6.822282114,7.028746406000002,6.118430299,6.285312759,6.559236744,7.163245982,6.945562889,7.474710503,7.601189842999999,7.5611432239999985,6.361671475,6.929216014,7.477935216,7.684420446,7.825531916,6.438668989,6.946354724,7.994465371,7.434118807000001,7.781988584,6.052318465,7.106650373,6.22094286,6.420457311,6.969249676,6.0113021810000005,6.600948787999999,7.817846496,6.8198271,7.291405641,7.598729065,6.157135092000001,7.1917274,7.418761774,6.488221135,6.044167236,6.010391864,6.949838549,7.907956251,7.639788459,7.53350946,6.251586885,6.543191814,7.651225301,6.708889665,6.625538653,6.528354932,6.450640306,7.181907673,7.016482298,6.388617138,7.57125447,7.609348255,7.137136973,6.354022554,6.196907944,7.829507245,6.395258356,7.992041984,6.583411671,6.206053072,6.976997772000001,6.562594972,7.260416405,6.460044777999999,6.699164936,7.401121811,6.912033409,7.764040111,7.796034006,6.969883482999999,6.730757538,6.601395755,6.465913274,6.41354791,6.475275337,6.407715561,6.550814117000001,7.36220835,7.36549204,7.8546243,7.995848977,6.725600855,7.786725333,7.656978112000001,7.105904818,7.199106204,7.871063004,7.566165721,6.7932454170000005,6.576261427,6.751452932,6.560743092999999,6.938313356,6.991626158,6.977700268,6.833768535,6.739170045,6.993473247000001,6.757470637000001,6.8506632320000005,6.74274935,6.506120752,6.98992719,6.69215564,6.544029776,6.927803911,6.721835879,6.99223441,6.704204398,6.702424548,6.641098708,6.585346229,6.563134737,6.502289472999999,6.800321319,6.721130542999999,6.574677594,6.919342407,6.519779582999999,6.687088097999999,6.747975732,6.65149129,6.502675132,6.825371185,6.99104104,6.5116248410000015,6.93172108,6.712772332999999,6.63016515,6.761953186,6.691202286,6.608667683999999,6.840802254,6.834808347999999,6.953439161,6.665024507999999,6.662875839,6.678695788,6.54277684,6.839443833,6.805277038,6.762522087000001,6.678449317999999,6.577192175,6.734005647999999,6.524459342,6.501521192,6.758479569,6.676578778,6.941496806,6.864143752,6.583528529,6.751747609,6.893509446,6.720744449,6.827812549,6.912299695,6.586107335,6.827305908,6.821774589,6.656458831,6.770384816,6.933809742999999,6.579441304,6.92791761,6.985804083,6.612429546,6.813383387000001,6.967759599999999,6.57398033,6.803094965,6.964955435,6.764213299,6.617703177999999,6.52711001,6.709668804,6.620729882000001,6.583760498999999,6.6764073370000006,6.751298936,6.867554147000001,6.7424900270000006,6.986228647000001,6.979102243,6.8256647820000005,6.617066674,6.551892637999999,6.598860305,6.4200187170000005,5.7400545670000005,5.686972967000001,6.293662362999999,6.381975465,5.542169138999999,5.551963184,5.8607404810000014,5.558807063,5.55771171,5.568365926,6.07071786,5.627860548999998,6.38488418,5.6858890660000005,6.234458417000001,6.443168642000001,5.842317989,5.955742971,5.741367375,5.948342571,6.387067562,5.562911913,5.85971872,6.282955072999999,6.25449571,5.973853124,6.081568052000001,6.37466756,6.027707171,5.868285082000001,6.205931637999999,5.5707453860000005,6.095261012999999,6.025789594,5.542873799,6.366219551,5.579845008,5.804965067,6.121005506,6.000248647,5.820978791,5.620733794,6.001936419,6.305740522000001,6.362544111,5.588655387,6.182232762000001,5.959493188,5.677282677999999,5.6121227970000005,6.206077742000001,5.764812076,6.203376525,6.143662699,6.100429497,5.7084096010000005,5.868255858,6.461225827000001,6.165084855,6.047044342,6.137102505,5.894027065,5.56222383,5.832608027999999,6.2185718739999984,6.142010637,6.078807239,5.702484758,5.547594847,5.836075368,6.231662767,5.718120393,5.852038202,5.547933273,6.156259104,6.436314406,5.981169595,6.271952832999999,6.470465614,6.141502001,5.826381164,6.342463714,6.071897347,6.331051715,6.413184638,5.50158009,6.338720873,6.015672239,5.735364307,6.465906333,5.855457599,6.318552972999999,6.006784979,6.008386282999999,5.665785202,5.764615485,5.901495543999999,5.779032666,5.67154928,7.231324765,6.925412377000001,7.633437412,6.827354668,6.176716425,6.6287228360000015,7.256877571,6.443785385,7.7232401510000015,5.947448589,7.2277455160000015,6.219469084,6.021439523,6.253343655,6.187455798999999,7.0576933660000005,6.720449769,6.4316895060000006,7.453106264,7.368258226,7.352401887,6.652143699,6.144631795,7.318802162000001,7.954629324,6.207652157,6.631005298,7.306918817000001,5.898293044,7.238566893,7.977651226,5.983075895,6.785723961,7.393441155,6.486068274,7.175934962,7.388265887999999,6.10539819,6.419536555,6.307585854,6.93221485,7.810865753,6.527541661,7.569454601,7.041065585,7.208795456,6.814341946,7.442217061,6.854558957,7.884550475,6.006085786,7.432043735,6.498052108,6.205263534,6.360812227,7.0466074339999984,7.947011366,6.281913857999999,6.114525877,6.7539780610000015,7.4250413160000015,6.745104394,7.6411165689999985,6.470135478,7.091992365,6.520403794,6.127939627999999,7.994679507000001,7.524707577,7.827877817999999,6.436691764,5.907930899,6.135025006,6.044556594,7.59781958,6.691268104,6.1754923060000015,7.272316208999999,5.801047545,6.757457943,6.983395572999999,7.976889497999999,6.558902588,7.979090365,7.903528672999999,6.73210948,6.6916904760000016,7.839849298,6.61448588,7.456971816,7.2942193,7.762647875,6.363406102000001,7.63737841,6.2006719760000015,6.364729934,6.913678684,7.766259768999999,7.55606399,7.288377241,6.002524871,6.033485257000001,7.121933578999999,6.207459637,6.090060478,6.346715209,6.661957897000001,6.176860192,7.251847296,6.386259977999999,7.319735475,6.025028997000001,6.344751947000001,7.02777956,7.299304715,7.014063944,7.4880144039999985,6.626503893,6.239011,6.742688094,6.588017308,7.097586415,6.956682742999999,7.380396262,6.176618831,6.551130445,6.427726565,6.740947635,6.130136384,6.667633355,6.1868143920000005,6.334837865,7.16214284,7.422318499,6.768001309,6.348441469,6.097294061,6.14132902,7.479248124,6.509174788999999,6.57256106,7.165696848,7.207457207999999,7.124333547000001,6.4635387070000005,6.856833064,7.132389299,6.235357637999999,6.704273839,7.433313409,6.109478059,7.095413294,6.352076782999999,6.6587699910000016,7.0518224720000005,7.333143205,6.352771037,7.124050134,6.998787171,6.537914957999999,7.171054239,7.228268227999999,7.319952206,6.613341342999999,6.096838784,6.132570522999999,7.36008498,7.321619041,7.175170657000001,7.299076163,6.842966478999998,6.356295567999999,6.508342839,7.098227926,6.310699968,7.093328631,6.691074249,6.187746776,6.491506245,6.855362875,7.124571593,6.067302109,6.432051512,6.253408852000001,7.287318722999999,7.161865733,6.065898282999999,7.311077075,6.581693772,6.732826127,6.014572075,6.663559451,6.434610995,7.432768147000001,6.987332927000001,6.718725189,6.880204617,6.86106911,6.7693455,7.26158085,7.261313694,7.235070264,7.18915558,6.431899747999999,6.42321105,6.869720196,6.973839707000001,7.184801627000001,6.351823783,6.392048018,6.119892347,6.910823945,6.501157208,7.027585558999999,7.13411409,6.6477659970000005,6.703270635,7.493191968,6.724688502999999,6.043485685,7.101661011,7.466900682999999,6.877799264,6.410992833,7.393825704,7.482414225,6.081172981,6.516312148,6.0433309510000015,6.959404135,7.238109556,7.234258375,6.691541233,6.809593554,6.485761419,6.784460602,7.167092586,6.73410539,6.779984384,7.277422737999999,7.21270048,7.487266991,7.231166546,6.559817161000002,6.979590627,6.779230041,6.217974349,7.205078785,6.854011265,6.246872394,6.911066044,6.777417989,6.273741983,6.906124587000001,7.162802357,6.9557873510000015,6.971963169,6.840927967000001,6.536676653,6.089443602999999,7.456460375,6.759211911,7.460174812000001,6.652642579,6.026287448,6.074190142000001,7.0455430560000005,6.9932360010000005,6.726528895,6.937352845,7.27905689,7.079850922,6.136286518,6.5052036960000015,7.042089492000001,6.348337518999998,7.432322234,6.787658922,6.743417121,7.00733163,7.303033217,6.861235184,7.131435858,7.288211994,6.983732393,6.172090205,6.35118177,6.908671378999999,6.766184468,6.392791654,6.3483162570000005,6.123796057000001,7.4285236339999985,6.020947179,6.334610249,6.78006386,6.086922359,6.362607851,6.758792552,6.779832611000002]