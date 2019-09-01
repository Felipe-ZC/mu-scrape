
#TODO: Handle case where DIR has a '/' at the end. 
#TODO: Improve arg parsing (getopt)

NAME=$([ $# -eq 0 ] && echo 'test' || echo $1) 
DIR=$([ $# -le 1 ] && echo 'results' || echo $2)
FILE=${DIR}/${NAME}.json

(rm ${FILE} || echo `No file named ${NAME} found`) && scrapy crawl news -o ${FILE}
#TODO: Why did ':%!python3 -m json.tool' work but not :%python3 -m json.tool'
#TODO Only run this command if the -f option is passed in to script...
#vim ${FILE} -c ':%!python3 -m json.tool'  
cat ${FILE}

printf '\nDone\n'
