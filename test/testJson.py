import json


msg = '''{"max":670,"unreadcounts":[{"id":"user/-/state/com.google/reading-list","count":670,"newestItemTimestampUsec":"1376221530480000"},{"id":"user/-/label/IT","count":497,"newestItemTimestampUsec":"1376221530480000"},{"id":"user/-/label/\u793e\u79d1","count":173,"newestItemTimestampUsec":"1376192467997000"},{"id":"feed/51f38d4f884abe6a7a000015","count":31,"newestItemTimestampUsec":"1376063871505999"},{"id":"feed/51f38d51884abe6a7a00002b","count":12,"newestItemTimestampUsec":"1374094381738000"},{"id":"feed/51f38d51884abe6a7a000038","count":67,"newestItemTimestampUsec":"1376064058692000"},{"id":"feed/51f38d52884abe6a7a00004d","count":16,"newestItemTimestampUsec":"1372524764688000"},{"id":"feed/51f38d52884abe6a7a00005f","count":2,"newestItemTimestampUsec":"1374915922335000"},{"id":"feed/51f38d52884abe6a7a000064","count":22,"newestItemTimestampUsec":"1376063917070000"},{"id":"feed/51f38d53884abe6a7a000079","count":20,"newestItemTimestampUsec":"1365908943228000"},{"id":"feed/51f38d54884abe6a7a00008e","count":20,"newestItemTimestampUsec":"1372960747853000"},{"id":"feed/51f38d5a884abe6a7a0000a4","count":10,"newestItemTimestampUsec":"1355301531025999"},{"id":"feed/51f38d5a884abe6a7a0000af","count":10,"newestItemTimestampUsec":"1355076767122000"},{"id":"feed/51f38d5e884abe6a7a0000bb","count":85,"newestItemTimestampUsec":"1376214335573000"},{"id":"feed/51f38d5e884abe6a7a0000d0","count":10,"newestItemTimestampUsec":"1363723959284999"},{"id":"feed/51f38d5e884abe6a7a0000db","count":20,"newestItemTimestampUsec":"1358564425034000"},{"id":"feed/51f38d6b884abe6a7a0000f1","count":23,"newestItemTimestampUsec":"1376069676008999"},{"id":"feed/51f38d6b884abe6a7a000106","count":21,"newestItemTimestampUsec":"1374966121751000"},{"id":"feed/51f38d6b884abe6a7a00011b","count":20,"newestItemTimestampUsec":"1373945927979000"},{"id":"feed/51f38d6b884abe6a7a000130","count":23,"newestItemTimestampUsec":"1376221530480000"},{"id":"feed/51f38d6c884abe6a7a000145","count":20,"newestItemTimestampUsec":"1374314769206000"},{"id":"feed/51f38d6c884abe6a7a00015a","count":22,"newestItemTimestampUsec":"1374521971636999"},{"id":"feed/51f38d6c884abe6a7a00016f","count":23,"newestItemTimestampUsec":"1376068166270000"},{"id":"feed/51f38d6c884abe6a7a000184","count":20,"newestItemTimestampUsec":"1370352541425000"},{"id":"feed/51f38d6c884abe6a7a00019a","count":10,"newestItemTimestampUsec":"1369632497833999"},{"id":"feed/51f38d70884abe6a7a0001a8","count":20,"newestItemTimestampUsec":"1363658441754000"},{"id":"feed/51f38d71884abe6a7a0001bd","count":20,"newestItemTimestampUsec":"1374232665649000"},{"id":"feed/51f38d71884abe6a7a0001d2","count":25,"newestItemTimestampUsec":"1376074006220000"},{"id":"feed/51f38d83884abe6a7a0001e8","count":21,"newestItemTimestampUsec":"1375164641197000"},{"id":"feed/51f38d84884abe6a7a0001fd","count":21,"newestItemTimestampUsec":"1376192467997000"},{"id":"feed/51f38d84884abe6a7a000212","count":14,"newestItemTimestampUsec":"1366568759177000"}]}'''

jsonObj = json.loads(msg)
print jsonObj["max"]
