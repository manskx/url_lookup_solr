import string
import random
def id_generator(size=50, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

query	=	"";

for x in range(0, 99999):
	query +="INSERT INTO `URL_Lookup`.`url_mapping` (`url_from`, `url_to`) VALUES ('"+id_generator()+"', '"+id_generator()+"'); \n"


f = open('QueryFile.sql','w')
f.write(query)
f.close()






