#TODO: Handle case where DIR has a '/' at the end. 
#TODO: Improve arg parsing (getopt)

#TODO: Make this an env var!
BASE_DIR='/home/zubuddy/projects/mu_scrape/src/news_spider'
NAME=$([ $# -eq 0 ] && echo test || echo $1) 
DIR=$([ $# -le 1 ] && echo ${BASE_DIR}/news_spider/util/results || echo $2)
FILE=${DIR}/${NAME}.json

(rm ${FILE} || echo `No file named ${NAME} found`) && scrapy crawl subpop -o ${FILE}
cat ${FILE}

printf '\nDone\n'\

#TODO: Why did ':%!python3 -m json.tool' work but not :%python3 -m json.tool'
#TODO: Only run this command if the -f option is passed in to script...
#TODO: Find out why this command messes up the encoding on FILE...
vim ${FILE} 
#-c ':%!python3 -m json.tool'
